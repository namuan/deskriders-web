+++ 
date = 2019-11-23T10:47:29Z
title = "Protecting applications with OAuth2 Proxy"
description = ""
slug = "" 
tags = ["docker", "oauth2", "security", "devops"]
categories = []
externalLink = ""
series = []
+++

Here is a simple guide on protecting a website with social logins supporting OAuth2. It uses an open source [OAuth2 Proxy](https://pusher.github.io/oauth2_proxy/) (which is a fork from [Bitly OAuth2 Proxy](https://github.com/bitly/oauth2_proxy)) to secure private applications without adding any authentication logic in the application itself. 

Here, we'll see how to secure the open source version of https://httpbin.org. Httpbin application itself is open and can be accessed without any authentication.

![Proxy configuration](/images/005/i1zmqplvv8eq8pzsvfvt.png)

In this guide, we will setup a Github OAuth application but the same setup can be easily configured with any other provider. See [Providers](https://pusher.github.io/oauth2_proxy/auth-configuration) for different config options.

#### Setting up Github Application:

Login to your github account and navigate to [Developer Settings](https://github.com/settings/developers). Click on OAuth Apps and Register a new application.

I'll call this application SocialBin and set the homepage as http://localtest.me. [Localtest.me](https://readme.localtest.me) is a DNS configured to point to 127.0.0.1 and makes it easy to do local testing.

We will be running the application on port 8080 so the callback url is set as http://localtest.me:8080/oauth2/callback.

That is it for setting up the application. Note down the Client ID and Client Secret which will be used later.

![Github Client configuration](/images/005/fozsrm840r7nu8wbia5o.png)

#### Running application with proxy:

Clone this [Github project](https://github.com/namuan/oauth2-proxy-httpbin) and then copy or move the example configuration file. 
```
cp .env.example .env
```

You can also run the following command to generate a random value which will be used for cookie secret.
```
head -c32 /dev/urandom | base64
```

Edit the .env file and update the variables. 
```
OAUTH2_PROXY_COOKIE_SECRET=<generated random value>
OAUTH2_PROXY_COOKIE_DOMAIN=http://localtest.me
OAUTH2_PROXY_CLIENT_ID=<github client id>
OAUTH2_PROXY_CLIENT_SECRET=<github client secret>
```

Now, switch over to docker-compose.yml which is setting up two docker containers. The [httpbin](https://hub.docker.com/r/kennethreitz/httpbin) container is the service we are trying to protect so you can see that it is not exposing any ports. The `"--upstream=http://httpbin:80",` configuration is telling the oauth2 proxy where to send the traffic once the login is successful.

With everything in its place, we can bring up the containers using `docker-compose`.
```
docker-compose up
```

It'll take some time if it is running for the first time to pull any missing docker images. Once everything is running, you can visit `http://localtest.me:8080/` in the browser which should show you a screen with a button to "Sign in with Github". Here is a brief sequence of the login flow and accessing httpbin.

![oauth2_proxy_login_httpbin](/images/005/br9iafvbj41srj5j7dxl.gif)

#### Conclusion:

As we saw, OAuth2Proxy is a useful tool to protect any application without changing the code. The source code for this setup is available here https://github.com/namuan/oauth2-proxy-httpbin. 

#### References:

https://github.com/pusher/oauth2_proxy
https://readme.localtest.me/
https://hub.docker.com/r/kennethreitz/httpbin
https://hub.docker.com/r/bitnami/oauth2-proxy
