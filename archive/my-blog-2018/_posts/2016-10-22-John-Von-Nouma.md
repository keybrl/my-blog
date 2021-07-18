---
layout: post
title: "从冯·诺依曼体系结构启航"
date: "2016-10-22"
description: "大一 “计算机导论Ⅰ” 课程的大作业，关于冯诺依曼体系结构对今天计算机发展的影响。"
image: images/John-Von-Nouma/title_image.jpg
---

## 1946

1946年2月14日，世界上第一台通用计算机“ENIAC”（ Electronic Numerical Integrator And Computer）在美国宾夕法尼亚大学诞生。这个30吨的大家伙运算速度比不上我们任何一个人手里的智能手机，但是他计算了不可计数的弹道模型，参与了第一颗原子弹的研制，而你不过使你手里的手机用弹弓发射小鸟来打猪。当然，这只是一个玩笑。我为什么要以这样一台大家伙的诞生开篇呢，答案很显然，这台计算机几乎是当下所有计算机的鼻祖，上至“天河二号”下至你手里的手机，无一例外。为什么说他是鼻祖，事实上在ENIAC之前还有“ABC”（一台只能进行线性方程组求解的计算机），主要是因为ENIAC能设定不同的程序，进行不同的工作，是一台通用计算机。“通用”对于计算机，在我看来是十分重要的，正如物理定理所追求的对于自然的普适。

ENIAC提供了一种通用的解决方案，但其实ENIAC在通用方面做得并不是特别优雅。在改变计算机功能的时候，需要进行繁琐的接线操作，有时这种操作需要持续几天，这甚至在很大程度上抵消了其运算速度优势，所以通用计算机需要新的思路。人类计算机的发展在1946年走出第一个黎明前的黑暗，其中正是ENIAC催生了人们的想象……



## 101页报告

冯·诺依曼（John von Neumann，1903-1957），在美国研制原子弹期间作为数学家参与原子弹研制工作。原子弹的研制涉及大量的计算，因此在原子弹研制后期，冯·诺依曼加入了ENIAC的研制小组。1945年6月，冯·诺依曼发表了一份长达101页的报告，题为“关于EDVAC的报告草案”（ First Draft of a Report on the EDVAC）。报告提出了我们今天仍广泛通用的计算机体系结构，也正是这份报告，催生了后来的EDSAC（Electronic Delay Storage Automatic Calculator）和EDVAC（Electronic Discrete Variable Automatic Computer）以及我们今天用的各式计算机。



## 冯·诺依曼体系结构

上文所说的101页报告中所提出的计算机体系结构，正是后来所说的“冯·诺依曼体系结构”，而冯·诺依曼本人也因此被称作“计算机之父”（尽管他本人并不接受）。

冯·诺依曼体系结构为我们提供了一种较于ENIAC更优雅的通用计算机的解决方案：

1. 冯·诺依曼体系结构的计算机必须具备5大组成部分，即：控制器、运算器、存储器、输入设备、输出设备；
2. 程序和数据均以二进制代码的形式不加区分地存储在存储器中，存储位置以地址标记；
3. 控制器根据存放在存储器中的程序指令进行工作，并由一个程序计数器控制指令的执行。控制器具有逻辑判断和算术运算能力，能根据计算结果选择不同的工作流程。

冯·诺依曼体系结构的核心就在于：计算机采用二进制进行工作；程序和数据都通过输入设备以二进制代码的形式输入；计算机按照程序顺序执行。或许，这些在我们现在看来都是十分理所当然的，但在那个年代却不是这样的。



## 黎明前的摸索

二进制在计算机上的应用，在今天看来是十分理所当然的。电子管、晶体管都是适合表示二进制的，二进制适合逻辑表示与运算……二进制除了在实用性方面有优势，在数学上也有形式上的美，从莱布尼茨开始，二进制的魅力就不断被人发掘，这我在此不作赘述。我们现在能说出很多关于二进制的好处，很大程度上因为我们已经在计算机上应用了二进制，正是与计算机的结合使二进制得以被广泛研究。其实，二进制并不是那么理所当然的，起码在冯·诺依曼之前的时代。每个正常的人都有十只手指，这个神奇的生理学特性使我们构建起了以十进制为根基的数学大厦。因此推翻十进制的优越性，在很多人看来是十分难以接受的，即使在今天，也存在相当一部分人认为十进制结构的计算机终会出现并取代二进制结构的计算机，这在我看来当然是不可能的。在冯·诺依曼的那个时代，存在着各种研究十进制、三进制或是其他非二进制计算机的努力。前苏联曾研制过三进制计算机，虽也能总结出不少好处，但仍以失败告终。连ENIAC也使用了不少十进制的工作方式并以十进制输入、输出。因此，冯·诺依曼体系结构在巩固二进制作为计算机工作方式方面无疑是做出了不少贡献的。

在冯·诺依曼之前，还有一位伟大的数学家对于计算机的发展功不可没，那就是艾伦·麦席森·图灵（Alan Mathison Turing，1912-1954）。图灵最早提出现代计算机的构想，即“图灵机”。图灵机是模仿人在运算时人思维的变化和注意力的移动是根据纸上数据的状态进行改变的而设计的假想机器。图灵机只是一种构想，而冯·诺依曼将其细化并实现了。图灵机的程序是事先写入机器的，可以看作是机器的一部分，正因为此，ENIAC的程序“写入”并不十分优雅，甚至可以说是痛苦。而冯·诺依曼则对此做出了改进，将数据和程序不加区别地由输入设备输入，存储在共同的存储器上，从而实现了计算机真正的通用。将程序也看作数据，这种思想在当时是十分难能可贵的。

黑暗中的摸索总是痛苦的，但当太阳升起，一切将焕发生机。



## 启航

冯·诺依曼体系结构的提出将人类计算机发展带到了新的纪元。此后经过不断的改进与发扬，冯·诺依曼体系结构迎来了前所未有的光明。在冯·诺依曼为我们铺就的道路上人类计算机事业飞速发展。

在继续叙述之前，我们先回顾一下冯·诺依曼体系结构。冯·诺依曼为我们提供的是一种优雅的通用的方法，它成功地发展了“图灵机”，使几乎所有数学问题都有了一种通用的解决方案，即冯·诺依曼体系结构。而在进一步的发展中，我们几乎能把所有的生活问题都转化为数学问题，这样，冯·诺依曼体系结构就成为了一种几乎能解决一切问题的通用解决方案，所以其精髓在于通用。“通用”之于计算机，正如我前文所说的，犹如“普适”之于自然定律。而在没有互联网思维、没有多用户的概念的时代，冯·诺依曼体系结构所蕴含的通用的思想无疑是超越时代的。也正是这样的思想，指导着软件开发从个人用户走向多用户，指导着计算机从单机走向互联。当下互联网的基础，TCP/IP协议族就处处渗透着通用的思想。

我们可以看到冯·诺依曼体系结构提供的只是一种通用的方法，但它并不是十分高效的。那是什么使冯·诺依曼体系结构得以流行呢？答案便是“摩尔定律”。

摩尔定律是由英特尔（Intel）创始人之一戈登·摩尔（Gordon Moore）提出来的。其内容为：当价格不变时，集成电路上可容纳的元器件的数目，约每隔18-24个月便会增加一倍。

现在流传着的摩尔定律有多种版本，但都离不开一点，即计算机的运算速度是呈指数函数增长的。极大的运算速度配合通用的解决方案，意味着极高的问题解决效率，这也正是冯·诺依曼体系结构的魅力所在。

至此，冯·诺依曼体系结构船在摩尔定律帆的驱动下启航。



## 帆船的尽头

在处理器性能越来越好，计算机越来越多的今天，在冯·诺依曼体系结构走向顶峰的同时，它也即将走到尽头。冯·诺依曼体系结构的墙或多或少已经出现在了我们面前：

1. 冯·诺依曼体系结构的计算机性能的提升与处理器性能的提升几乎是一阶线性相关的，这就使计算机的发展难以跟上人类文明的发展；
2. 摩尔定律从某种程度上已经失效，一道更高的墙拦在处理器性能的提升上；
3. 随着计算机越来越深入地参与人类的生活，计算机已不仅仅是一种数学工具，在解决生活问题的过程中，冯·诺依曼体系结构产生了愈发明显的语义间隔，即“冯·诺依曼语义间隔”。这使得计算机非专业人员难以深入挖掘计算机的能力。

人类计算机发展即将进入新的黑夜。正如帆船无法突破风速，冯·诺依曼体系结构也遇到了无法超越的极限。



## 重新启航

在冯·诺依曼体系结构广泛应用的同时，人类突破禁锢，研究“非冯·诺依曼体系结构”的努力从未停止：

1. 哈佛体系结构。冯·诺依曼体系结构使用统一的存储器不加区分地存储程序和数据，并使用一条总线与处理器相联，这使得计算机读取程序和读取数据只能在时间上相间进行，这使得存储器读取效率十分的低，加上当下存储器的读取速率已限制了处理器的发展，因此冯·诺依曼体系结构的工作效率难以提高。哈佛体系结构使用两个独立的存储器和总线，用于程序和数据的分别存储与传输。读取程序与读取数据可以同时互不干扰地执行，这能极大地提高工作效率。
2. 神经网络计算机。冯·诺依曼体系结构在计算机中广泛使用，但世界上最强大的“计算机”——人脑，却不使用冯·诺依曼体系结构。在处理复杂现实问题的时候，现有任何计算机都比不上人脑。因此，人们试图让计算机模拟人脑的工作方式，设计通过多个微处理器、类似于神经的节点和并行的算法模拟人脑的思维方式以处理复杂的多元的问题。
3. 量子计算机。冯·诺依曼体系结构使用二进制，很大程度上是因为电子元件更易于表现出两种稳定的状态。但微观粒子可以较容易地表现出多种量子态，量子计算机可以使用数十进制，而且量子态的改变较于电子元件状态的改变要迅速得多，这使得量子计算机的运算速度可以远超冯·诺依曼体系结构的电子计算机。其次，量子态存在不确定性，量子态可以叠加，这些性质使得量子计算机完全区别于冯·诺依曼体系结构的计算机。冯·诺依曼体系结构的计算机同一时间只能有一种机器状态、只能串行处理程序，而量子计算机可以并行地处理程序，这使得量子计算机有着极高的工作效率。

不可否认，冯·诺依曼体系结构是人类计算机发展之路上极为重要的里程碑，所以我们愉快地走过，收拾心情，继续前行。风帆驱动的木船不能突破风速，所以我们需要使用内燃机驱动的快艇。人类计算机发展的旅程才刚刚开始，下一个黎明，我们将重新启航。