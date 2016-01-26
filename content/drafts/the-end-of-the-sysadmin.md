Title: The End of the Sysadmin
Date: 2016-01-31 19:30
Category: self-hosting
Tags: self-hosting, decentralization
Slug: the-end-of-the-sysadmin
Author: Dražen Lučanin
Author_link: https://cloudfleet.io/blog/meet-our-team-drazen.html
Summary: The need for human sysadmins does not scale. We need open source platform commons.


## Beyond Self-Hosted Apps

We have already talked quite a bit about the importance of self-hosting
your apps due to the limitations of
[centralized cloud services][cloud-limitations]
and mentioned a number of [great apps][tools] ready for self-hosting.
In this blog post, we therefore assume that you do self-host your apps
to protect your [data autonomy][data-autonomy].
From here, we take the discussion to the next step and look at
what happens after you set up an app on your hardware and how do you maintain
it, a job done in typical organisations by professional system administrators,
aka sysadmins.


## Human Sysadmins Do Not Scale

In this decentralized dream, we quickly see that having a human sysadmin for
every personal data center is a luxury. Either in terms of money needed to
hire one or the personal time needed to stay informed and on top of
all the current security threats. Security vulnerabilities are found almost
daily! To name a few recent popular ones: [Heartbleed](http://heartbleed.com/),
[Shellshock](https://en.wikipedia.org/wiki/Shellshock_%28software_bug%29),
[Logjam](https://weakdh.org/) and [FREAK](https://freakattack.com/)...
(come on, there's gotta be a song hiding in there with
all these nice exploit names 😀)

It is true that knocking down doors the way the NSA can do with Facebook's or
Google's to get direct data access doesn't scale for a decentralized cloud.
Finding and exploiting security vulnerabilities scales very well, though.
With tools like [Metasploit][], you don't need much more than a "script
kiddie" to build a [botnet][]. From the always popular
[old routers][router-botnet]
and [Wordpress sites][wordpress-botnet], to the more fashionable
[IoT botnets built from refrigerators][iot-botnet] and
[botnets spanning the whole internet][large-botnet], the dangers are evident and
*very exploitable*.

What if the current package where people start out with a Linux image
for a Raspberry Pi and are on their own from there on is too low-level?


## Open Source Platform Commons

We believe that the right level of abstraction for decentralizing the web is not
by providing only operating system images, but by providing a platform.
A platform where after installing that first self-hosted app,
the user can still easily get
automatic updates for security patches. One that includes the collective wisdom
of the crowd, made transparent through an open source project.
In a way, the *open source platform commons*.

**1. Auto-Updates**

Heroku did a great thing for application development, allowing developers to
set up their clients with apps that are deployed to a platform where Heroku's
sysadmins handle the operations, freeing the app owners of needing dedicated
engineers to handle day-to-day operations. We need something like this for
self-hosting apps too.

We recently announced this on Twitter:

<blockquote class="twitter-tweet" lang="en"><p lang="en" dir="ltr">How to Protect Yourself from NSA Attacks on the recently discovered Diffie-Hellman vulnerability - <a href="https://t.co/pcNccSr97r">https://t.co/pcNccSr97r</a> /HT <a href="https://twitter.com/EFF">@EFF</a></p>&mdash; cloudfleet.io (@cloudfleetio) <a href="https://twitter.com/cloudfleetio/status/655420616200298496">October 17, 2015</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

Of course, at the time this came out, we had [already hardened][nginx-fix]
our nginx configuration. All of the CloudFleet Blimps got this patch through
the nightly [auto-updates][auto-updates] we provide as part of the CloudFleet
Services.

**2. Openness and Trust**

The other key component is that we need to know that we can trust this group of
people that is pushing updates to us. For example, we love using [Signal][]
for messaging internally and as [Mark][] nicely put it:

> I trust Signal only because of one man - [Moxie Marlinspike][moxie]

Signal is built as an open source project by people who transparently discuss
its development in the open and are serious about security. This immediately
gives it more credibility than closed source apps like WhatsApp that claim e2e
encryption or even some semi-open apps like Telegram that came under criticism
from [multiple][telegram-attack1] [sides][telegram-attack2] recently.

We are striving to develop CloudFleet in an open and trustworthy manner as well,
with all of the source code and protocols published as
[open source][cloudfleet-github]. We are ready to discuss all aspects of our
project on [our public (self-hosted) forum][forum].

As we are striving to decentralize the Internet through self-hosting using
projects like the Raspberry Pi, we are asking more and more people to keep track
of everything that is going on in the
security sphere, which is simply not possible without investing a lot of time.
The end goal where every person has their own hardware device for storing their
data will invariably mean *the end of the sysadmin* and nececitate
open source platform commons. Take a look at this CloudFleet
[technical overview][] to see how we are building one in the open and,
if you are interested, consider
backing our [crowdfunding campaign][crowdfunding].

[forum]: https://discourse.cloudfleet.io/
[cloudfleet-github]: https://github.com/cloudfleet
[Signal]: https://whispersystems.org/
[Mark]: https://cloudfleet.io/blog/meet-our-team-mark.html
[auto-updates]: http://cloudfleet.readthedocs.org/en/latest/doc/technology/technology.html#architecture
[Metasploit]: https://www.metasploit.com/
[botnet]: https://en.wikipedia.org/wiki/Botnet#Illegal_botnets
[router-botnet]: https://voidsec.com/en/aethra-botnet-en/
[iot-botnet]: http://www.ibtimes.co.uk/spam-emails-are-being-sent-by-your-fridge-1432737
[wordpress-botnet]: http://arstechnica.com/security/2013/04/huge-attack-on-wordpress-sites-could-spawn-never-before-seen-super-botnet/
[large-botnet]: http://www.theregister.co.uk/2013/03/19/carna_botnet_ipv4_internet_map/
[data-autonomy]: https://cloudfleet.io/blog/introducing-data-autonomy.html
[cloud-limitations]: https://cloudfleet.io/blog/5-reasons-to-self-host.html
[nginx-fix]: https://github.com/cloudfleet/blimp-nginx/pull/1/files
[tools]: https://cloudfleet.io/blog/tools-to-take-back-control-over-your-data.html
[moxie]: https://en.wikipedia.org/wiki/Moxie_Marlinspike
[telegram-attack1]: http://www.alexrad.me/discourse/a-264-attack-on-telegram-and-why-a-super-villain-doesnt-need-it-to-read-your-telegram-chats.html
[telegram-attack2]: http://thoughtcrime.org/blog/telegram-crypto-challenge/
[crowdfunding]: https://www.indiegogo.com/projects/cloudfleet-your-private-encrypted-cloud-at-home/x/4096670#/
[technical overview]: http://cloudfleet.readthedocs.org/en/latest/doc/technology/technology.html
[cloudfleet]: https://cloudfleet.io/
