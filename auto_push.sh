#!/bin/bash


echo"email_address:"
EMAIL = read()

echo("username:")
USERNAME = read()

echo("passwd:")
PASSWD = read()

git add --all

git config --global user.email "$EMAIL_R"

git remote add origin www.github.com/$USRNAME/$CANGKU

git remote rm oringin

git remote add origin git@github.com:$USRNAME/$CANGKU

git push -u origin master
