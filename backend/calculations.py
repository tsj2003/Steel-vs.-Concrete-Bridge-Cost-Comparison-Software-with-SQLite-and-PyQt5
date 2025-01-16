def calculate_costs(data, material_data):
    length = data["length"]
    width = data["width"]
    traffic_volume = data["traffic_volume"]
    design_life = data["design_life"]

    # Extract material rates
    base_rate = material_data["base_rate"]
    maintenance_rate = material_data["maintenance_rate"]
    repair_rate = material_data["repair_rate"]
    demolition_rate = material_data["demolition_rate"]
    environmental_factor = material_data["environmental_factor"]
    social_factor = material_data["social_factor"]
    delay_factor = material_data["delay_factor"]

    # Calculate costs
    construction_cost = length * width * base_rate
    maintenance_cost = length * width * maintenance_rate * design_life
    repair_cost = length * width * repair_rate
    demolition_cost = length * width * demolition_rate
    environmental_cost = length * width * environmental_factor
    social_cost = traffic_volume * social_factor * design_life
    user_cost = traffic_volume * delay_factor * design_life
    total_cost = (construction_cost + maintenance_cost + repair_cost +
                  demolition_cost + environmental_cost + social_cost + user_cost)

    return {
        "construction_cost": construction_cost,
        "maintenance_cost": maintenance_cost,
        "repair_cost": repair_cost,
        "demolition_cost": demolition_cost,
        "environmental_cost": environmental_cost,
        "social_cost": social_cost,
        "user_cost": user_cost,
        "total_cost": total_cost,
    }
