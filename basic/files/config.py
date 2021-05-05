import yaml

cf = open('./basic/files/config.yaml')
cfyaml = yaml.load(cf, Loader=yaml.FullLoader)

print(cfyaml)