#!/usr/bin/env python
# coding: utf-8

# # Linear Regression

# ## Formulation

# The governing equation for linear regression can be expressed as:
# 
# \begin{equation} 
# \mathbf{Y} = \mathbf{\beta}\mathbf{X} + \epsilon, 
# \end{equation}
# 
# where,
# 
# $$
#   \begin{align*}
#     \mathbf{Y} &= \begin{bmatrix}
#            y_{1} \\
#            y_{2} \\
#            \vdots \\
#            y_{n}
#          \end{bmatrix}
#   \end{align*},
#   \begin{align*}
#     \mathbf{\beta} &= \begin{bmatrix}
#            \beta_{1} \\
#            \beta_{2} \\
#            \vdots \\
#            \beta_{m}
#          \end{bmatrix}
#   \end{align*}, 
#   \begin{align*}
#     \mathbf{X} &= \begin{bmatrix}
#            x^T_{1} \\
#            x^T_{2} \\
#            \vdots \\
#            x^T_{n}
#          \end{bmatrix}
#   \end{align*},
#   \begin{align*}
#     \mathbf{\epsilon} &= \begin{bmatrix}
#            \epsilon_{1} \\
#            \epsilon_{2} \\
#            \vdots \\
#            \epsilon_{n}
#          \end{bmatrix}
#   \end{align*}.
#   $$
# 
# 
# $\mathbf{Y}$ is the target variable, $\mathbf{X}$ is the feature matrix, $\epsilon$ is the error term or intercept and $\mathbf{\beta}$ is the vector of coefficients. 

# The aim is to find solutions for the coefficients and error term such that
# 
# \begin{equation}
# \tilde{\mathbf{Y}} = \mathbf{\beta}\mathbf{X} + \epsilon, 
# \end{equation}
# 
# that minimises $\mathbf{Y} - \tilde{\mathbf{Y}}$

# 
