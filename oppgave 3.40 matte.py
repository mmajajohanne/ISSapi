#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 08:56:47 2021

@author: majamarjamaa
"""

#gjennomsnittlig vekstfart

x = 1
øvre = 1.01

dy=(3*øvre+1)/(øvre-2)-(3*x+1)/(x-2)
dx = øvre-x
gvf = dy/dx

print("Den gjennomsnittlige vekstfarten for intervallet er", gvf)