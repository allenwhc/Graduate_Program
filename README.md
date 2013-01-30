<<<<<<< HEAD
# ![Pinry](https://raw.github.com/dotcom900825/grad_project/master/xishi.jpg)

Xi Shi is based on [Pinry](https://github.com/overshard/pinry/) project, which is a private, self-hosted, [Pinterest][0] inspired by [Wookmark][1] and
built on top of Django. 


This project is forked from Pinry and then co-developed by several students in BUPT together.


![Pinry Screenshot]()


## Why?

We develop Xi Shi as a social networking website for college student initially. However, Xi Shi is different from Facebook or twitter where people can update their status or follow other people. We establish social relationship by exchanging things. Student in our campus(Beijing University of Posts and Telecommunication) can trade or exchange their book or digital equipment etc with other student and hopefully meet new friend in the same time.

## Getting Started

Pinry has two different customizable configurations:


### Development

* Have virtualenv and pip installed.

* You may also need to have the build
dependencies for PIL installed. (PIL is the Python Image Library, mainly for process the picture the user uploaded) Note: On Ubuntu you can get the build deps by running
`sudo apt-get build-dep python-imaging`.
* Create virtualenv on your development environment first, Suppose we gonna create two folder on our Desktop, one named as `Sites` and another named `virtualenv`  
* First go to Sites folder and clone the git repo, then create virtualenv in virtualenv folder
* Next activate virtualenv and start install all the needed Python module
* Sync Database
* Use South migrate database 
* Run the development server

####Example

    $ cd ~/Desktop
    $ mkdir sites
    $ mkdir virtualenv
    $ cd sites
    $ git clone https://github.com/dotcom900825/grad_project
    $ cd ~/Desktop/virtualenv
    $ virtualenv grad_project
    $ source grad_project/bin/activate
    $ cd ~/Desktop/sites/grad_project
    $ pip install -r development.txt
    $ python manage.py syncdb
    $ python manage.py migrate
    $ python manage.py runserver


### Production

If you want a production server [Google around][2] for more information on
running Django in a production environment and edit the
`pinry/settings/production.py` file. 

### Quick Settings

There are a few settings provided specific to Pinry that allow you to get some
of the most requested functionality easily.

 + **SITE_NAME**: For quickly changing the name Pinry to something you prefer.
 + **ALLOW_NEW_REGISTRATIONS**: Set to False to prevent people from registering.
 + **PUBLIC**: Set to False to require people to register before viewing pins.
   (Note: Setting PUBLIC to False does still allow registrations. Make sure
          both PUBLIC and the previous setting are set to False to prevent
          all public access.)





## License (Simplified BSD)

Copyright (c) Isaac Bythewood  
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice,
   this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


[0]: http://pinterest.com/
[1]: http://www.wookmark.com/
[2]: https://www.google.com/search?q=deploy+django+production
=======
Graduate_Program
================

Online Trading
>>>>>>> af0189502c5d667e96b99a83b470a722adf0df20
