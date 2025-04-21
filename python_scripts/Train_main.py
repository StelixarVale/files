from DQN import DQN_episoid
from Project_config import path_list

def main():
    # 调用DQN进行抓取训练
    DQN_episoid.DQN_episoid()
    # PPO_episoid()

if __name__ == '__main__':
    print("_________")
    with open(path_list['resetFlag'], 'r+') as file:
        file.write('1')
    main()
