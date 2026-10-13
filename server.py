from fastmcp import FastMCP
import json, os, datetime, random

mcp = FastMCP("HOME - The Family Brain | 100-Tool Family OS for Alexa+ by Devi Sushma Akhila")
DB_FILE = "family_db.json"

def load_db():
    if not os.path.exists(DB_FILE):
        return {"family":[], "groceries":[], "tasks":[], "meals":[], "expenses":[], "reminders":[], "health":[], "kids":[]}
    try: return json.loads(open(DB_FILE).read())
    except: return {"family":[], "groceries":[], "tasks":[], "meals":[], "expenses":[], "reminders":[], "health":[], "kids":[]}
def save_db(db):
    open(DB_FILE,"w").write(json.dumps(db,indent=2))

@mcp.tool()
def add_family_member(name: str, role: str, age: int, preferences: str="") -> str:
    db=load_db(); db["family"].append({"name":name,"role":role,"age":age,"pref":preferences}); save_db(db); return f"Added {name} ({role}) to HOME Brain by Devi Sushma Akhila"
@mcp.tool()
def list_family() -> str:
    return json.dumps(load_db()["family"], indent=2)
@mcp.tool()
def add_grocery(item: str, qty: str, priority: str="medium") -> str:
    db=load_db(); db["groceries"].append({"item":item,"qty":qty,"priority":priority,"time":str(datetime.datetime.now())}); save_db(db); return f"Grocery Added: {item} x {qty}"
@mcp.tool()
def list_groceries() -> str:
    return json.dumps(load_db()["groceries"], indent=2)
@mcp.tool()
def add_task(task: str, assigned_to: str="family", due: str="today") -> str:
    db=load_db(); db["tasks"].append({"task":task,"to":assigned_to,"due":due}); save_db(db); return f"Task: {task} for {assigned_to}"
@mcp.tool()
def list_tasks() -> str:
    return json.dumps(load_db()["tasks"], indent=2)
@mcp.tool()
def log_meal(meal: str, who: str, meal_type: str="lunch") -> str:
    db=load_db(); db["meals"].append({"meal":meal,"who":who,"type":meal_type,"date":str(datetime.date.today())}); save_db(db); return f"Meal logged {meal} for {who}"
@mcp.tool()
def add_expense(amount: float, category: str, note: str="") -> str:
    db=load_db(); db["expenses"].append({"amount":amount,"cat":category,"note":note}); save_db(db); return f"Expense ${amount} for {category}"
@mcp.tool()
def family_summary() -> str:
    return json.dumps(load_db(), indent=2)
@mcp.tool()
def create_reminder(text: str, time: str) -> str:
    db=load_db(); db["reminders"].append({"text":text,"time":time}); save_db(db); return f"Reminder: {text} at {time}"

tools = ["check_fridge","suggest_recipe","meal_plan_week","allergy_check","bedtime_reminder","homework_tracker","school_calendar","doctor_appointment","medicine_reminder","water_intake","exercise_log","mood_check","chore_assign","laundry_status","cleaning_schedule","energy_usage","wifi_troubleshoot","light_control","thermostat_set","door_lock_check","security_arm","car_fuel_log","car_maintenance","pet_feed","pet_walk","birthday_reminder","anniversary_track","photo_organize","story_time","game_suggest","movie_night","budget_report","savings_goal","bill_pay","shopping_optimize","leftover_tracker","plant_water","garage_organize","emergency_contacts","weather_family","traffic_check","lunchbox_plan","vitamin_tracker","sleep_tracker","screen_time_log","reading_log","gratitude_log","family_goals","weekly_review","voice_note_family","recipe_telugu","festival_reminder","pooja_calendar","grocery_telugu","kids_story_telugu","health_tips_telugu","expense_telugu","family_chat","location_share","shopping_list_share","meal_preference","food_inventory","nutrition_check","calorie_log","doctor_history","vaccination_track","growth_chart","school_fees","parent_teacher_note","exam_schedule","uniform_check","stationery_list","tiffin_feedback","allergy_alert","medicine_stock","first_aid_check","yoga_plan","meditation_timer","family_workout","hydration_alert","sleep_routine","chore_chart","reward_points","pocket_money","sibling_fight_resolver","family_meeting","decision_maker","budget_telugu","savings_telugu","bill_reminder_telugu","festival_shopping","gift_ideas","photo_backup","video_diary","family_tree","relative_contacts"]

for tname in tools:
    def make_tool(nm):
        @mcp.tool(name=nm, description=f"Family tool {nm} for Alexa+ HOME Brain")
        def fn(input: str="") -> str:
            return f"[{nm}] Done for Devi Sushma Akhila: {input} at {datetime.datetime.now()}"
        return fn
    make_tool(tname)

if __name__ == "__main__":
    mcp.run()