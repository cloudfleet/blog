Title: 9 Tools to Take Back Control over Your Data
Date: 2015-12-11 10:30
Category: self-hosting
Tags: self-hosting, decentralization
Slug: tools-to-take-back-control-over-your-data
Author: Christoph Witzany
Author_link: https://cloudfleet.io/#team-4
Summary: Awesome tools that help you escape the tyranny of cloud services.
Status: published


## Tools for You

The first 4 tools we present are for your personal use; they will enable you to
have the experience of a cloud service withouit giving up control over your data.

While cloud services like GMail and Dropbox are convenient, there are [many good
reasons](https://cloudfleet.io/blog/5-reasons-to-self-host.html) why you should
not rely on them too much.

## 1. Read Mails with Mailpile

[Mailpile](https://mailpile.is) aims at providing a state of the art email
client. The project was started by Bjarni Runar Einarson of [Pagekite](https://pagekite.net)
fame.

Mailpile creates a powerful index of all your emails to make them easily
searchable. It also makes it very easy to send and receive encrypted emails.

You can run Mailpile on you own machine, but if you want an even easier start,
just wait for your CloudFleet Blimp. **CloudFleet will use Mailpile as its email
client.**

Alternative solutions are [Roundcube](https://roundcube.net/) and
[Nylas N1](https://nylas.com/N1).

## 2. Synchronize Contacts and Calendars with Radicale

Synchronizing your contacts and calendar entries across different devices can be
a pain if you don't want to use Google for that. [Radicale](http://radicale.org) is a
server that enables this using the open protocols CalDAV and CardDAV, which are
understood by all modern devices.

**With your CloudFleet Blimp you will get Radicale automatically.**

If you don't like Radicale or just have a PHP server at your disposal, you can also use [DAViCal](http://davical.org/)

## 3. Keep Notes with Braindump

Every now and then it is necessary to scribble down a note. Be it a shopping
list or the plan to take over the world, you don't want everybody to know about
it. So instead of the centralized Evernote you should use
[Braindump](https://braindump.pw/).

**Braindump will also be available on your CloudFleet Blimp.**

Like always there are more possibilities to choose from, eg.
[Laverna](https://laverna.cc/) or [OpenNote](https://foxusa.github.io/OpenNote/).

## 4. Sync Files with the Server Formerly Known as Ubuntu One

Dropbox sure is convenient; but are you sure you want to store your private
files with a service that *has* to hand it over to the authorities if requested?

Ubuntu once tried to create a service similar to Dropbox but canceled it.
However they released the code to the public, giving the world a battle-tested
[file synchronization server](https://github.com/dboudwin/filesync-server) that
can be used to host the data at home.

Various clients for many operating systems are also available.

**You can synchronize your files with your CloudFleet Blimp.**

[Seafile](https://www.seafile.com/en/home/) is also a product that allows you
to synchronize your files.

## Tools for Your Organization

What is true for you personally is just as true for your organization. The
following 5 tools allow you to escape the claws of cloud services and also attain
 data sovereignty for your company or non-profit.

## 5. Collaborate on Your Code with GitLab

To develop software in a team, a good version control system is important and a
central repository with a web interface makes the collaboration much easier.

The people from [GitLab](https://about.gitlab.com/) created a tool that makes it easy
to host this at your own premises. If you ever used GitHub, you will soon find
yourself at home with GitLab.

**At CloudFleet we use GitLab to host the code for our internal projects.**

A project with similar scope is [Gogs](https://gogs.io/).

## 6. Use Mattermost to Chat

Quick and frictionless communication is the lifeblood of every team. With
[Mattermost](http://www.mattermost.org/) there's now a powerful competitor
to the centralized Slack.

It's easy to install and if you already use GitLab, it's included.

**[Let's chat](http://sdelements.github.io/lets-chat/) is another tool which we
actually use at CloudFleet, as Mattermost wasn't yet ready when we started using
self-hosted chat.**


## 7. Use Taiga to Organize

No project can be successful without a place where all the information about
tasks and issues is concentrated. [Taiga](https://taiga.io) is a modern tool for
agile teams that allows you to manage your user stories, sprints and issues.

You can also add a wiki to the project and use a central user directory to
authenticate your users.

**At CloudFleet we use Taiga to manage our tasks, user stories and issues.**

If Taiga doesn't suit your needs, [OpenProject](https://www.openproject.org/) serves a similar purpose.

## 8. Piwik

To get data about how many people visit a web page and where they come from is
of uttermost importance for every business nowadays. Most services, however,
demand that you store your data with them.

Fortunately there is [Piwik](https://piwik.org), a self hosted service that
makes it possible to keep this essential data under your own control.

**At CloudFleet we use Piwik to count the traffic on our web page without
disclosing your information to Google via Google Analytics, like most web pages.**

## 9. Discourse

[Discourse](https://discourse.org) is the new project by Jeff Atwood of
[Stack Overflow](https://stackoverflow.com) and
[Coding Horror](http://blog.codinghorror.com/) fame. It makes it easily
possible to host a state of the art discussion forum and if you want you can use
it to enable discussions on your static web pages, like on this blog.

Now it's your turn! Have you used any of the tools we outlined above? Are there any you're currently using which we haven't mentioned? Let us know in the comments, we'd love to hear from you about the tools you use to take back control over your data.
