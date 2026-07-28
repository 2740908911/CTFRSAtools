# CTFRSAtools


## Abstract

* This tool is designed for the automatic determination, analysis, and solving of RSA-type problems within the Crypto category of CTF competitions.

* CTFRSAtools (hereinafter referred to as CRts) supports script expansion, allowing other scripts encountered during competitions to be timely added to the tool. In essence, CRts acts as an RSA script container and integrates common tools for RSA problem types found in CTFCrypto. You can customize CRts by adding, supplementing, or even modifying scripts. Nearly 20 scripts for common problem types have already been included, which can satisfy the basic formats of RSA problems in most competitions. If you need to expand the scripts, please ensure the script format refers to other existing script files. Script expansion is detailed below.

* CRts does not include SageMath scripts. Therefore, for problems involving finite field square roots, Coppersmith's high-bit plaintext attack, Franklin-Reiter attack, polynomials, etc., please implement those manually.

* CRts supports public key decomposition and file decryption; specific usage methods are detailed below.

* For usage instructions, other issues, and help, please see below.


## Structure and Logic

**CRts Structure**

```
CTFRSAtools
/example	# data.txt examples
	-- omitted
/RSAtools	# Script storage and calling
	-- omitted
--banner.py
--main.py
--RSAjudge.py	# Add identification information here

Attached
data.txt	# Problem data
flag.enc	# Encrypted file
pub.key		# Public key file
readme.md	# File documentation
```

**Design Logic:**

CRts serves as a problem-solving container and adopts a separation of scripts and judgment to maximize the tool's customizability.

CRts reads data via `data.txt` rather than command-line input, ensuring that data is repeatedly readable and easy to modify and check.

CRts requires Python 3 support. The development version used is Python 3.8; please pay attention to library installations during use.


## Features and Notes

**Features:**

```
# Features will be continuously added and modified with version updates; 
# please refer to the actual runtime effect of CRts.
# Scripts may be added after each competition. If you have new ideas, 
# you can contact the author to join the GitHub project team for collaborative development.
# For feature examples, see <Usage and Testing>.

+ Mutual solving for standard RSA problem types (details omitted)
+ Large number factorization based on factordb.com and yafu
+ dp leak attack
+ dp, dq leak attack
+ Common modulus attack
+ Low decryption exponent attack (large e)
+ Wiener's attack
+ Public key decomposition
+ File decryption
```

**Notes:**

1. Since `factordb` is used when factoring N, a network connection is required; if no network is available, `yafu` will be used for factorization, which may be inefficient for very large numbers. You may also factorize manually on factordb.com or via yafu and then write the results into `data.txt`.
2. SageMath is not currently equipped in CRts, so Sage-based scripts cannot be added to the script set.
3. Some functions may be imperfect. To avoid unnecessary errors, please ensure that every value in `data.txt` is useful.
4. When using this tool, you should have a basic foundation in RSA. If bugs occur during problem-solving, you can adjust the parameters based on the analysis and provide feedback promptly.


## Download and Installation

**Download:**

CRts is not yet open-source (scripts are being continuously improved; it will be released once the effect is satisfactory—currently, it can only solve simple problems).

CRts is hosted on GitHub. Interested developers can contact the author for collaborative development.

**Installation:**

```
1. git clone or download 

2. Install python3 (skip if already installed)

3. pip install gmpy2

4. pip install Crypto

5. pip install RSA

6. pip install numpy

7. Install any other missing libraries...

8. Run tests
```

For installation issues, please refer to Baidu (especially for steps 3 and 4).

An .exe version is expected to be released after open-sourcing (Note: the .exe version may not support custom scripts).


## Usage and Testing

**Usage Instructions:**

1. Before use, ensure that data has been written to `data.txt` in the CRts root directory or saved in `pub.key`/`flag.enc` files.
2. Open cmd or powershell and `cd` to the CRts root directory.
3. `python main.py`
4. Once the script runs automatically, wait for the results to return. If there are no results or there is a bug, please contact the author.
5. Please clear the `data.txt`, `pub.key`, and `flag.enc` files promptly after use for the next session.

**Testing Examples:**

> The example problem data are all selected from CTFshow and buuCTF.
>
> The examples below are shown out of order and are unrelated to the sequence of features.

<!--p-->

![b9b5225684d4f0a1c1dab39aa492ae6f.png](http://img.imfanqie.xyz/images/2022/05/25/b9b5225684d4f0a1c1dab39aa492ae6f.png)

![7e02342279d2641abc7bc54c92c9ed6a.png](http://img.imfanqie.xyz/images/2022/05/25/7e02342279d2641abc7bc54c92c9ed6a.png)

![ec274f31481dfed3a503fe11eed37614.png](http://img.imfanqie.xyz/images/2022/05/25/ec274f31481dfed3a503fe11eed37614.png)

![61ffc40146d6d83dee5511fbfa97d945.png](http://img.imfanqie.xyz/images/2022/05/25/61ffc40146d6d83dee5511fbfa97d945.png)

![52ceae63a122db7c49ca637cc0f0549c.png](http://img.imfanqie.xyz/images/2022/05/25/52ceae63a122db7c49ca637cc0f0549c.png)

![54aab50011f3a9d9bc9d5b0bb818f8aa.png](http://img.imfanqie.xyz/images/2022/05/25/54aab50011f3a9d9bc9d5b0bb818f8aa.png)

![e734dd9a4caf01462a617b0af59cdeec.png](http://img.imfanqie.xyz/images/2022/05/25/e734dd9a4caf01462a617b0af59cdeec.png)

![48e37229d386fa9425615eab652fc3ca.png](http://img.imfanqie.xyz/images/2022/05/25/48e37229d386fa9425615eab652fc3ca.png)

![37c0ded11a20d6dbd7febafb3720d782.png](http://img.imfanqie.xyz/images/2022/05/25/37c0ded11a20d6dbd7febafb3720d782.png)


## Custom Extension

> When using this method, please ensure you have a certain understanding of RSA-type problems and have referred to other scripts in `RSAtools`.

If you need to customize scripts (delete, modify, or add), you can refer to the following section.

* Please review other scripts in `RSAtools` beforehand:

  * Here is an example based on the format of most files:
    The `solves()` function serves as the basic interface function for solving the problem, facilitating calls from other scripts.
    The `printf()` function serves as the print function, calling `solves()` for calculation and returning the result to the screen.
  * The format for calling other scripts is `from RSAtools import xxxxx`.
  * If the calculation result is `d`, you can refer to the following format:

  ```python
  def printf(e,p,q):
      d = solves(e,p,q)
      print("=" * 99)
      print("int_d：" + str(d))
      print("=" * 99)
  ```

  * If the calculation result is `m`, you can refer to the following format:

  ```python
  def printf(x,y,z):
  	m = solves(x,y,z)
  	print("=" * 99)
  	try:
  		print("int：" + str(m))
  		print("hex：" + str(hex(m)))
  	except:
  		print("int：" + str(m))
  
  	try:
  		print("hex to ascii：" + str(binascii.unhexlify(hex(m)[2:])))
  	except:
  		try:
  			print("libnum(n2s)：" + str(libnum.n2s(hex(m))))
  		except:
  			print("just hex or int ")
  	print("=" * 99)
  ```

* After writing the new script according to the format, add the judgment conditions to `RSAjudge.py`.

  + In the `fun_call()` function, you can see all method calls; when adding a script, you can also add it to this function for use.
  + In the `judge(RSAdata)` function, you can determine the data classification based on the prints and comments, then add your script to the corresponding category.

+ If you have new elements to define, such as `r`, `x`, `y`, `z`, etc., you can follow the implementation in `main.py` to assign values.


## Version and Updates

**Version Log**

| Name        | Version   | Date      | Log and Remarks               |
| ----------- | --------- | --------- | ---------------------------- |
| CTFRSAtools | beta 0.1  | 2022.5.24 | Base version, future updates TBD |
|             |           |           |                              |
|             |           |           |                              |

**Planned Goals**

* Add SageMath scripts.
* Expand the RSA problem-solving scope and add solving methods for other types of problems.
* Integrate other cryptography types to expand the application range of the tools, such as: Base family, base conversion, encoding conversion, MD5 targeted brute-forcing, etc.
* TBD...


## Closing

This document was written based on the initial version. Due to updates, there may be differences from the actual product; this description is for reference only.

This project is for learning and competition purposes only. Private distribution or sharing without permission is prohibited!

Other developers are welcome to join and help improve the tool. The project repository is not public; please contact the author for the project address.

> Author: Fanqie
>
> Contact: q/v 2740908911
>
> Last Edited: 2022/5/25
