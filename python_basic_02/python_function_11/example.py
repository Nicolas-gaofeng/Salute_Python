#!/usz/bin/env python
# -*- coding:utf-8 -*-

"""
@author     : zgf
@brief      : function——example
"""

# ========================================= 函数 =========================================
# 模块化编程思想：自顶向下，分而治之
# 【问题描述】
# 小丹和小伟羽毛球打的都不错，水平也在伯仲之间，小丹略胜一筹，基本上，打100个球，小丹能赢55次，小伟能赢45次。
# 但是每次大型比赛（1局定胜负，谁先赢到21分，谁就获胜），小丹赢的概率远远大于小伟，小伟很是不服气。
# 亲爱的小伙伴，你能通过模拟实验，来揭示其中的奥妙吗？
# 【问题抽象】
# 1、在小丹Vs小伟的二元比赛系统中，小丹每球获胜概率55%，小伟每球获胜概率45%；
# 2、每局比赛，先赢21球（21分）者获胜；
# 3、假设进行n = 10000局独立的比赛，小丹会获胜多少局？（n 较大的时候，实验结果≈真实期望）
# if flag:
# flag = True
flag = False
if flag:

    def get_inputs():
        # 输入原始数据
        prob_A = eval(input("请输入运动员A的每球获胜概率(0~1)："))
        prob_B = round(1 - prob_A, 2)
        number_of_games = eval(input("请输入模拟的场次（正整数）："))
        print("模拟比赛总次数：", number_of_games)
        print("A 选手每球获胜概率：", prob_A)
        print("B 选手每球获胜概率：", prob_B)
        return prob_A, prob_B, number_of_games

    # 单元测试
    prob_A, prob_B, number_of_games = get_inputs()
    print(prob_A, prob_B, number_of_games)

    def sim_n_games(prob_A, prob_B, number_of_games):
        # 模拟多场比赛的结果
        win_A, win_B = 0, 0  # 初始化A、B获胜的场次
        for i in range(number_of_games):  # 迭代number_of_games次
            score_A, score_B = sim_one_game(prob_A, prob_B)  # 获得模拟依次比赛的比分
            if score_A > score_B:
                win_A += 1
            else:
                win_B += 1
        return win_A, win_B

    import random

    def game_over(score_A, score_B):
        # 单场模拟结束条件，一方先达到21分，比赛结束
        return score_A == 21 or score_B == 21

    def sim_one_game(prob_A, prob_B):
        # 模拟一场比赛的结果
        score_A, score_B = 0, 0
        while not game_over(score_A, score_B):
            if random.random() < prob_A:  # random.random() 生产[0,1)之间的随机小数,均匀分布
                score_A += 1
            else:
                score_B += 1
        return score_A, score_B

    def print_summary(win_A, win_B, number_of_games):
        # 结果汇总输出
        print("共模拟了{}场比赛".format(number_of_games))
        print("选手A获胜{0}场，占比{1:.1%}".format(win_A, win_A / number_of_games))
        print("选手B获胜{0}场，占比{1:.1%}".format(win_B, win_B / number_of_games))

    def main():
        # 主要逻辑
        prob_A, prob_B, number_of_games = get_inputs()  # 获取原始数据
        win_A, win_B = sim_n_games(prob_A, prob_B, number_of_games)  # 获取模拟结果
        print_summary(win_A, win_B, number_of_games)  # 结果汇总输出

    if __name__ == "__main__":
        main()
