#!/bin/bash
seq 1 111 | nc 83.136.250.111 44292 | tee temp.log

