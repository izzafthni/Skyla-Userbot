Skip to content
Kayzyu
/
Kayzu-Ubot
Public template
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
Kayzu-Ubot/Dockerfile
@Kayzyu
Kayzyu Update Dockerfile
 2 contributors
17 lines (13 sloc)  520 Bytes
# Using Python Slim-Buster
FROM kyyex/kyy-userbot:buster
#━━━━━ Userbot Telegram ━━━━━
#━━━━━ By Skyla-Userbot ━━━━━

RUN git clone -b Skyla-Userbot https://github.com/SkylaIND/Skyla-Userbot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/Kayzyu/Kayzu-Ubot/Kayzu-Ubot/requirements.txt

EXPOSE 80 443

# Finalization
CMD ["python3", "-m", "userbot"]
© 2022 GitHub, Inc.
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
Loading complete
