from setuptools import setup

setup(name='visualCaptchaTornado',
      version='0.0.5',
      description='Python Distribution Utilities',
      author='Junior Gregoire',
      author_email='junior.gregoire@gmail.com',
      url='https://github.com/juniorGreg',
      packages=['visualcaptchatornado'],
      install_requires=["tornado", "visualcaptcha", "torndsession"]
     )