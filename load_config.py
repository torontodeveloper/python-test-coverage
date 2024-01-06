import argparse
import yaml

CONFIG_PATHS =['system_config.yml','user_config.yml','job_config.yml']

parser = argparse.ArgumentParser()

parser.add_argument('job_config',type=str)

args = parser.parse_args()
paths_to_load = CONFIG_PATHS + [args.job_config]
print(args)

config = {}

for path in paths_to_load:
    print('Loading',path)
    with open(path,'r') as file:
        this_config = yaml.safe_load(file)
        print('this config',this_config)
    
    config.update(this_config)
    
    
print(f'config is {config}')