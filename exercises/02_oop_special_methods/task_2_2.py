# -*- coding: utf-8 -*-
'''
Задание 2.2

Скопировать класс PingNetwork из задания 1.2 и изменить его таким образом,
чтобы адреса пинговались не при вызове метода scan, а при вызове экземпляра.

Вся функциональность метода scan должна быть перенесена в метод, который отвечает
за вызов экземпляра.

Пример работы с классом PingNetwork. Сначала создаем сеть:
In [2]: net1 = IPv4Network('8.8.4.0/29')

И выделяем несколько адресов:
In [3]: net1.allocate('8.8.4.2')
   ...: net1.allocate('8.8.4.4')
   ...: net1.allocate('8.8.4.6')
   ...:

Затем создается экземпляр класса PingNetwork, сеть передается как аргумент:
In [6]: ping_net = PingNetwork(net1)

После этого экземпляр должен быть вызываемым объектом (callable):

In [7]: ping_net()
Out[7]: (['8.8.4.4'], ['8.8.4.2', '8.8.4.6'])

In [8]: ping_net(include_unassigned=True)
Out[8]: (['8.8.4.4'], ['8.8.4.2', '8.8.4.6', '8.8.4.1', '8.8.4.3', '8.8.4.5'])


'''
