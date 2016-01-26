Title: The End of the Sysadmin
Date: 2016-01-31 19:30
Category: self-hosting
Tags: self-hosting, decentralization
Slug: the-end-of-the-sysadmin
Author: Dražen Lučanin
Author_link: https://cloudfleet.io/blog/meet-our-team-drazen.html
Summary: The need for human sysadmins does not scale. We need open source platform commons.


## Self-Hosting Apps

- previous posts on self-hosting [tools][tools]
- only real technical way to ensure data autonomy

## Human sysadmins do not scale

- too many exploits (heartbeat, shellshock, FREAK SSL/TLS, Logjam, SSL outdated protocols... come on, there's gotta be a song hiding in there with all these nice exploit names 😀)

- Nginx update tweet

<blockquote class="twitter-tweet" lang="en"><p lang="en" dir="ltr">How to Protect Yourself from NSA Attacks on the recently discovered Diffie-Hellman vulnerability - <a href="https://t.co/pcNccSr97r">https://t.co/pcNccSr97r</a> /HT <a href="https://twitter.com/EFF">@EFF</a></p>&mdash; cloudfleet.io (@cloudfleetio) <a href="https://twitter.com/cloudfleetio/status/655420616200298496">October 17, 2015</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

- at the time this came out, we bad [already hardened][nginx-fix] our
nginx configuration - and that of all our users through nightly security updates

- Wordpress
- stats on bot-farms
- number of vulnerable routers etc.

## Open Source Platform Commons

- auto-updates
- trusted open source communities; as Mark put it:

> I trust Signal only because of one man - [Moxie Marlinspike][moxie]

- the operating system level does not cut it, it needs to happen
on the platform level
- something like Heroku did for application deployment, allowing developers to
set up their clients with apps, without dedicated operations people
- We need something like this for app self-hosting.
- we need

As we are striving to decentralizing the Internet through self-hosting using
projects like the Raspberry Pi, we are asking more and more people to keep track
of everything that is going on in the
security sphere, which is simply not possible without investing a lot of time.
The end goal where every person has their own hardware device for storing their
data will invariably mean *the end of the sysadmin* and nececitate
open source platform commons. Take a look at this CloudFleet
[technical overview][] to see how we are building one in the open and,
if you are interested, consider
backing our [crowdfunding campaign][crowdfunding].

[nginx-fix]: https://github.com/cloudfleet/blimp-nginx/pull/1/files
[tools]: https://cloudfleet.io/blog/tools-to-take-back-control-over-your-data.html
[moxie]: https://en.wikipedia.org/wiki/Moxie_Marlinspike
[telegram-attack1]: http://www.alexrad.me/discourse/a-264-attack-on-telegram-and-why-a-super-villain-doesnt-need-it-to-read-your-telegram-chats.html
[telegram-attack2]: http://thoughtcrime.org/blog/telegram-crypto-challenge/
[crowdfunding]: https://www.indiegogo.com/projects/cloudfleet-your-private-encrypted-cloud-at-home/x/4096670#/
[technical overview]: http://cloudfleet.readthedocs.org/en/latest/doc/technology/technology.html
[cloudfleet]: https://cloudfleet.io/
