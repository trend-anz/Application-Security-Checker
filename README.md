# Cloud One: Application Security Checker
## About

Inspired by Workload Security's [Cloud Connector](https://help.deepsecurity.trendmicro.com/feature-releases/aws-add.html#What),  Application Security Checker advises users which Lambdas are secured and which ones aren't. 

## Example

```
python3 app-sec-checker.py

DemoLabda-01: False
DemoLabda-02: False
DemoLabda-03: False
DemoLabda-04: False
DemoLabda-05: False
DemoLabda-06: False
DemoLabda-07: True
DemoLabda-08: False
DemoLabda-09: False
DemoLabda-10: False
DemoLabda-11: False
DemoLabda-12: False
DemoLabda-13: False

12/13 (92.31%) of Lambdas are unprotected.
```