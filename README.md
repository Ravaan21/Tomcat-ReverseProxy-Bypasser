# This is based on CVE-2018-11759 -Deserialization

The Apache Web Server (httpd) specific code that normalized the requested path before matching it to the URI-worker map in Apache Tomcat JK (mod_jk) Connector 1.2.0 to 1.2.44 did not handle some edge cases correctly. If only a sub-set of the URLs supported by Tomcat were exposed via httpd, then it was possible for a specially constructed request to expose application functionality through the reverse proxy that was not intended for clients accessing the application via the reverse proxy. It was also possible in some configurations for a specially constructed request to bypass the access controls configured in httpd. While there is some overlap between this issue and CVE-2018-1323, they are not identical. (CVE-2018-11759)


What does the Program do?
It logically bypasses filters which are present in Apache Tomcat by comparing it through a set of sensitive directories and appending the logic of bypass with it.

Web servers and reverse proxies normalize the request path. For example, the path /image/../image/ is normalized to /images/. When Apache Tomcat is used together with a reverse proxy such as nginx there is a nromalization inconsistency.

Tomcat will threat the sequence /..;/ as /../ and normalize the path while reverse proxies will not normalize this sequence and send it to Apache Tomcat as it is.

This allows an attacker to access Apache Tomcat resources that are not normally accessible via the reverse proxy mapping.

**Installation:**

sudo apt install dirb

git clone https://github.com/Ravaan21/Tomcat-ReverseProxy-Bypasser.git

python3 TomTraversalBuster.py

Note: This only will display result if the server is vulnerable.
Check the path and the host, make sure you don't add www and add https or http depending upon SSL.

![Demo-min](https://user-images.githubusercontent.com/48627542/137644121-3e8631fe-ed22-4f08-a333-cb1792af36de.gif)

