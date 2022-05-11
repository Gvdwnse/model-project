#Model Project

#Importing the modules and packages to be used in this project
from scipy import optimize
import numpy as np

#a. Writing out the objective functions to be optimized
h_ss_func = lambda h, alpha=(1/3), phi=(1/3), g=0.015, sk=0.2, sh=0.15, n=0, delta=0.06: h-(((sk**alpha)*(sh**(1-alpha)))/(n+g+delta+n*g))**(1/(1-alpha-phi))

y_ss_func = lambda y, alpha=(1/3), phi=(1/3), g=0.015, sk=0.2, sh=0.15, n=0, delta=0.06, A=1: y-((((sk/(n+g+delta+n*g))**(alpha/(1-alpha-phi)))*(sh/(n+g+delta+n*g))**(phi/(1-alpha-phi)))*A)

#b. Now we can define the optimizer function
def bisect2(a, b, alpha=(1/3), phi=(1/3), g=0.015, sk=0.2, sh=0.15, n=0, delta=0.06):
    """ bisection
    
    Args:
    
        a      (float)          : one end of the bracketing interval [a,b]
        b      (float)          : the other end of the bracketing interval [a,b]
        alpha  (float)          : income share of capital and labour
        phi    (float)          : income share of human capital and labour
        g      (float)          : growth rate of technology
        sk     (float)          : savings rate of physical capital
        sh     (float)          : savings rate of human capital
        n      (float)          : growth rate of labour
        delta  (float)          : depreciation rate on human- and physcial capital
    
    Returns:
    
        steady state value for h(tilde)^*
        
    """
        
    alpha = alpha
    sk = sk
    sh = sh
    n = n
    g = g
    phi = phi
    delta = delta
    return optimize.bisect(h_ss_func, a, b)

#And the second one
def bisect3(a, b, alpha=(1/3), phi=(1/3), g=0.015, sk=0.2, sh=0.15, n=0, delta=0.06, A=1):
    """ bisection
    
    Args:
    
        a      (float)          : one end of the bracketing interval [a,b]
        b      (float)          : the other end of the bracketing interval [a,b]
        alpha  (float)          : income share of capital and labour
        phi    (float)          : income share of human capital and labour
        g      (float)          : growth rate of technology
        sk     (float)          : savings rate of physical capital
        sh     (float)          : savings rate of human capital
        n      (float)          : growth rate of labour
        delta  (float)          : depreciation rate on human- and physcial capital
        A      (float)          : technology
    
    Returns:
    
        steady state value for y^*
        
    """
        
    alpha = alpha
    sk = sk
    sh = sh
    n = n
    g = g
    phi = phi
    delta = delta
    A = A
    return optimize.bisect(y_ss_func, a, b)

#Extended model with government tax (tau)

#a. Objective functions for h and y respectively

h_ex_ss_func = lambda h, alpha_ex=(1/3), phi_ex=(1/3), g_ex=0.015, sk_ex=0.2, n_ex=0, delta_ex=0.06, tau_ex=0.15: h-((sk_ex/(n_ex+g_ex+n_ex*g_ex+delta_ex+tau_ex))*((tau_ex**(1-alpha_ex))/((n_ex+g_ex+n_ex*g_ex+delta_ex+tau_ex)**(1-alpha_ex))**(1/(1-alpha_ex-phi_ex))))

y_ex_ss_func = lambda y, alpha_ex=(1/3), phi_ex=(1/3), g_ex=0.015, sk_ex=0.2, n_ex=0, delta_ex=0.06, tau_ex=0.15, A_ex=1: y-(A_ex*(((tau_ex/(n_ex+g_ex+delta_ex+n_ex*g_ex))**(phi_ex/(1-alpha_ex-phi_ex)))*((sk_ex/(n_ex+g_ex+delta_ex+n_ex*g_ex+tau_ex))**((alpha_ex+phi_ex)/(1-alpha_ex-phi_ex)))))

#b. optimizer functions for h (and y below)
def bisect5(a, b, alpha_ex=(1/3), phi_ex=(1/3), g_ex=0.015, sk_ex=0.2, n_ex=0, delta_ex=0.06, tau_ex=0.15):
    """ bisection
    
    Args:
    
        a      (float)          : one end of the bracketing interval [a,b]
        b      (float)          : the other end of the bracketing interval [a,b]
        alpha  (float)          : income share of capital and labour
        phi    (float)          : income share of human capital and labour
        g      (float)          : growth rate of technology
        sk     (float)          : savings rate of physical capital
        sh     (float)          : savings rate of human capital
        n      (float)          : growth rate of labour
        delta  (float)          : depreciation rate on human- and physcial capital
        tau    (float)          : government tax rate
    
    Returns:
    
        steady state value for h(tilde)^*
        
    """
        
    alpha_ex = alpha_ex
    sk_ex = sk_ex
    n_ex = n_ex
    g_ex = g_ex
    phi_ex = phi_ex
    delta_ex = delta_ex
    phi_ex = phi_ex
    tau_ex = tau_ex
    return optimize.bisect(h_ex_ss_func, a, b)

# optimizer function for y
def bisect6(a, b, alpha_ex=(1/3), phi_ex=(1/3), g_ex=0.015, sk_ex=0.2, n_ex=0, delta_ex=0.06, tau_ex=0.15, A_ex=1):
    """ bisection
    
    Args:
    
        a      (float)          : one end of the bracketing interval [a,b]
        b      (float)          : the other end of the bracketing interval [a,b]
        alpha  (float)          : income share of capital and labour
        phi    (float)          : income share of human capital and labour
        g      (float)          : growth rate of technology
        sk     (float)          : savings rate of physical capital
        sh     (float)          : savings rate of human capital
        n      (float)          : growth rate of labour
        delta  (float)          : depreciation rate on human- and physcial capital
        tau    (float)          : government tax rate
        A      (float)          : technology
    
    Returns:
    
        steady state value for y(tilde)^*
        
    """
        
    alpha_ex = alpha_ex
    sk_ex = sk_ex
    n_ex = n_ex
    g_ex = g_ex
    phi_ex = phi_ex
    delta_ex = delta_ex
    phi_ex = phi_ex
    tau_ex = tau_ex
    A_ex = A_ex
    return optimize.bisect(y_ex_ss_func, a, b)
