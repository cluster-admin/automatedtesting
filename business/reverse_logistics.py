from common.robot import Robot

class Reverse_logistics():


    def reverse_logistics(self):
        '''逆向物流'''
        Robot().task_import()
        Robot().task_status()
        Robot().asser_code(150)
        Robot().arrive_early() #上料点提前到达
        #判断是否docking失败
        Robot().resume_sub_task()#顶升异常--点击完成
        Robot().arrive_early() #停靠点提前到达
        #判断顶升下降后执行undocking
        Robot().resume_sub_task()  # undocking--点击完成
        Robot().arrive_early() #空料架点--提前到达
        #docking异常
        Robot().resume_sub_task()  # 顶升异常--点击完成
        #判断前往下料点
        Robot().arrive_early()  # 下料点提前到达
        #判断undocking异常
        Robot().resume_sub_task()  # 顶升异常--点击完成
        #判断状态：空闲，任务状态完成




if __name__ == '__main__':
    pass






    

