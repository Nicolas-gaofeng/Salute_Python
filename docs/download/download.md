## Python

[Python](https://www.python.org/getit/)

## Anaconda

[Anaconda](https://www.anaconda.com/products/individual)是一个很好用的Python IDE，它集成了很多科学计算需要使用的python第三方工具包。

根据自己的操作系统安装好[Anaconda](http://www.continuum.io/downloads)后，在命令行下输入：

```python
conda list 
```

第一次安装好 [Anaconda](http://www.continuum.io/downloads) 以后，可以在命令行输入以下命令使 [Anaconda](http://www.continuum.io/downloads) 保持最新：

```python
conda update conda
conda update anaconda 
```

conda 是一种很强大的工具，具体用法可以参照它的[文档](http://conda.pydata.org/docs/)。

也可以参考它的 [cheat sheet](http://conda.pydata.org/docs/_downloads/conda-cheatsheet.pdf) 来快速查看它的用法。

可以使用它来安装，更新，卸载第三方的 **python** 工具包：

```python
conda install <some package>
conda update <some package>
conda remove <some package> 
```

在安装或更新时可以指定安装的版本号，例如需要使用 `numpy 1.8.1`：

```python
conda install numpy=1.8.1
conda update numpy=1.8.1 
```

查看 `conda` 的信息：

```python
conda info
```

一个很棒的功能是 `conda` 可以产生一个自定义的环境，假设在安装的是 **Python 2.7** 的情况下，想使用 **Python 3.7**，只需要在命令行下使用 `conda` 产生一个新的环境：

```python
conda create -n py37 python=3.7 
```

这里这个环境被命名为 `py37` ，可以根据喜好将 `py37` 改成其他的名字。

使用这个环境时，只需要命令行下输入：

```python
activate py37 #(windows)
source activate py37 #(linux, mac)

```

此时，我们的 **Python** 版本便是 python 3.7了。

