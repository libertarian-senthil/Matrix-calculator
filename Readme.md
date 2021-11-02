# Matrix Calculator:  

<details>
  <summary><b>Table of content</b></summary>  
  
1. [Overview](#Overview)
2. [Current version](#Current-version)  
3. [Current progress](#Current-progress)  
</details>  

---

## Overview  
> Welcome to matrix calculator project. We're focused on developing a GUI based calculator to perform __*Matrix*__ based operations. In today's world there are websites here to do this matrices operations. But we aim at developing this calculator application to be installed on the **PC** so that it is easy to make calculation rather than waiting for an website to load. the key feature of using this application is, it is an open source software, anyone can see the code behind and as a user no need to worry about accepting cookies or visiting or redirected towards an ad-sites, and many more.  

---
## Current version
The current version of the project is `version-0.1.1`.
---

### Features of version-0.1.0  

> *Version-0.1.0*   
**Release date:** Not for release 

* All the arithmetic operations of matrices can be done.  

* `Command line interface` for end user. In future versions **GUI** will be integrated.  
---
### Features of version-0.1.1  

> *Version-0.1.1*   
**Release date:** 4th November(expected)
* Additional functionality or formula are added.  

---
## Current progress

* `main.py`(matrix_project\\[main.py](https://github.com/libertarian-senthil/Matrix-calculator/blob/main/matrix_project/main.py)) -> New options added namely:  
1. Addition    
2. Subtraction  
3. Multiplication  
4. Square of a matrix  
5. Transpose  
6. Exit  

* We can give the input of No. of dimensions in runtime itself which is useful for non-programmers to choose what the dimensions needed, but yet to make multi dimension for multiplication of matrices.

* In `arithmetic.py`(matrix_project\matrix\)[arithmetic.py](https://github.com/libertarian-senthil/Matrix-calculator/blob/main/matrix_project/matrix/arithmetic.py) addtion, subtraction and multiplication methods work has been completed.  

* \#1 Issue was resolved but it in future the file organisation might be required for `main.py` since it is currently placed inside the `matrix package`.  

* New module (i.e. file) created to the `matrix package`  called `formula.py` (matrix_project\\[formula.py](https://github.com/libertarian-senthil/Matrix-calculator/blob/main/matrix_project/matrix/formula.py)) -> Structure is developed and Square of a matrix is completed but, it needs to be changed into exponent and the transpose functionality(i.e. method) is on progress.  
