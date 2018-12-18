---
author: gbmhunter
date: 2014-08-15 04:19:48+00:00
draft: false
title: Non-Standard GNU C/C++ Features (aka Extensions)
type: page
url: /programming/compilers/gcc/non-standard-gnu-cc-features-aka-extensions
---

# Overview

GNU offers some non-standard features in their C and C++ compilers. They call these extensions. I do not recommend using extensions where possible, they are extremely compiler specific and make your code less portable.

That said, they are still sometimes the best tool for the job (e.g. you can't do something any other way, or the non-compiler specific method is ugly and horrible).

# Initialisation Priorities

GNU allows you to determine the initialisation order of **global static variables** by specifying a priority.
    
    ```c++
    // In some .cpp file...
    
    MyClass myVar1  __attribute__ ((init_priority (321)));
    MyClass myVar2  __attribute__ ((init_priority (12)));
    ```

Usually, myVar1 would be initialisaed before myVar2. However, with myVar2 being specified with the priority 12 (lower numbers equate to a higher priority), myVar2 will be initialised first.