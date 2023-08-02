#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 18 10:19:47 2022

@author: majamarjamaa

fysikk kjernereaksjon

235U + nøytron -> 141Ba + 92Kr + 3n
"""
u = 1.66e-27
c = 3e8

m_elektron = 0.000549*u
m_nøytron = 1.008664*u


#kjernemasser
m_U235 = 235.043930 * u - 92*m_elektron
m_Ba141 = 140.914411 * u - 56*m_elektron
m_Kr92 = 91.926156*u - 36*m_elektron

m_før =  m_nøytron + m_U235
m_etter = m_Ba141 + m_Kr92 + 3*m_nøytron

dm = m_før - m_etter

print(f"Frigjort energi er E={round(dm*c**2*10**12,2)} pJ")
