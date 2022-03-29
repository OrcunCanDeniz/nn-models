import json

stats = {
    "VEHICLE" : {
            "L1": {"AP": 0.7044,
                    "APH": 0.6992},
            "L2":{  "AP": 0.6216,
                    "APH": 0.6169}
            },
    
    "PEDESTRIAN" : {
                "L1" : {"AP": 0.7359,
                        "APH": 0.6258},
                "L2" : {"AP": 0.6559,
                        "APH": 0.5562}
                },
    "SIGN" : {
            "L1": {"AP": 0.0,
                    "APH": 0.0},
            "L2": {"AP": 0.0,
                    "APH": 0.0}
            },                
    "CYCLIST" :{ 
        "L1": {"AP": 0.6521,
                "APH": 0.6371},
        "L2": {"AP": 0.6278,
                "APH": 0.613}
        }
}

acc_ap = 0
acc_aph = 0
ap_cnt = 0
aph_cnt = 0

for cls in stats:
    if cls != "SIGN":
        for dif in stats[cls]:
            acc_ap += stats[cls][dif]["AP"]
            acc_aph += stats[cls][dif]["APH"]
            ap_cnt += 1
            aph_cnt += 1

means = {"mAP" : acc_ap/ap_cnt,
        "mAPH" : acc_aph/aph_cnt}
means.update(stats)

# Serializing json 
json_object = json.dumps(means, indent = 4)
  
# Writing to sample.json
with open("metrics.json", "w") as outfile:
    outfile.write(json_object)