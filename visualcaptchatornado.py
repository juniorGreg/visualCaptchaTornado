from visualcaptcha import Session, Captcha
from torndsession.sessionhandler import SessionBaseHandler


class VisualCaptchaRequestHandler(SessionBaseHandler):

    def get(self, cmd, arg=None):
        if cmd == "start":

            visualCaptcha = Captcha(Session(self.session.session))

            visualCaptcha.generate(int(arg))
            self.write(visualCaptcha.getFrontendData())

        elif cmd == "audio":
            visualCaptcha = Captcha(Session(self.session.session))

            headers = {}
            result = visualCaptcha.streamAudio(headers, 'mp3')
            self.write(result)

        elif cmd == "image":
            visualCaptcha = Captcha(Session(self.session.session))

            headers = {}
            result = visualCaptcha.streamImage(headers, int(arg))
            self.write(result)

    def post(self, cmd):
        if cmd == "try":
            if self.trySubmission():
                self.write("Submission is valid.")
            else:
                self.send_error(403)

    def trySubmission(self):
        if self.request.arguments["valid"][0] == "false":
            return False

        visualCaptcha = Captcha(Session(self.session.session))
        frontendData = visualCaptcha.getFrontendData()

        if frontendData is None:
            return False

        if frontendData['imageFieldName'] == self.request.arguments["name"][0]:
            imageFieldName = self.request.arguments["value"][0]
            return visualCaptcha.validateImage(imageFieldName)
        elif frontendData['audioFieldName'] == self.request.arguments["name"][0]:
            audioFieldName = self.request.arguments["value"][0]
            return visualCaptcha.validateAudio(audioFieldName)
        else:
            return False
