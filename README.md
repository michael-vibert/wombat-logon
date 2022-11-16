# Wombat Logon

Welcome to Wombat Logon, the only terminal application you will ever need for storing your passwords. Handy, efficient and places the power to remain secure right in your hands. 

## 3 Features of Wombat Logon

1. Secure Authentication of the User
2. Strong Password Generator
3. Easy and convenient access to saved login credentials

### Description of the features

### 1.
The first feature is my implementation of a system the securely authenticates the User. This means that only the owner of the User account and all of the associated credentials will be able to access the account. This will be implemented using a secure Master Passphrase for the system. It will need to be supplied along with the correct login details or else access will be denied. 
### 2. 
We all know how challenging it is to come up with good passwords that are strong and at the same time we will remember. So my second feature is a dynamic random password generator. Leave the remebering part to Wombat Logon and use our random generator to create a strong password with all of the variables in your control. For example in you would like a password with 5 lower case letters, 3 numbers, 1 special character and 2 uppcase letters then all you have to do is select those details and a random password will appear. 
### 3. 
Having a bunch of secure passwords isn't any good to you unless you can conveniently access them when you need them! So Wombat Logon makes your life easy. Just type in your website, and we will return your password in plain text ready to go. Ta da!

## Plan to this stage

I have a high level overview of the major sections of this project. 
Below is a flowchart created

![flowchart of high level app](./images/Wombat%20Logon.drawio.png)

link to my [trello board](https://trello.com/b/5ibuUPZm) documenting my project management. 

## Progress Feature One

I have developed a more detailed flow chart of feature one detailed below:
![Detail flow chart of Feature One](./images/Wombat%20Logon%20Feature%20One.drawio.png)

## Proposed Classes and functions

### Class User
1. create account
2. save User
3. user_logon
4. verify_user

### Class Crypto
1. encypt
2. decrypt
3. read_file
4. write_file
5. load_data
6. hash_password

### Class NewUser
1. collect_credentials
2. check_credentials
3. warn_user_master_password

### Class MenuScreen
1. menu