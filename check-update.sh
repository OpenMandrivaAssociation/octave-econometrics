#!/bin/sh
package=econometrics
curl -L https://gnu-octave.github.io/packages/${package}/ 2>/dev/null |sed -ne "s,.*${package}-,,;s,\.tar.\gz,,p" |head -n1

