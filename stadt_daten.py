import requests

class data:
    def init(self, stadt):
        self.stadt = stadt

        api_key = "9e27ecdb4c485a76f67bb3d315df1e4f"

        url = f"https://api.openweathermap.org/data/2.5/weather?q={stadt}&appid={api_key}&units=metric"

        data = requests.get(url).json()

        coord = data["coord"]
        weather = data["weather"]
        weather_id = weather["id"]
        weather_main = weather["main"]
        weather_description = weather["description"]
        weather_icon = weather["icon"]
        base = data["base"]
        main = data["main"]
        main_temp = main["temp"]
        main_feels_like = main["feels_like"]
        main_temp_min = main["temp_min"]
        main_temp_max = main["temp_max"]
        main_pressure = main["pressure"]
        main_humidity = main["humidity"]
        visibility = data["visibility"]
        wind = data["wind"]
        wind_speed = wind["speed"]
        wind_deg = wind["deg"]
        clouds = data["clouds"]
        clouds_all = clouds["all"]
        dt = data["dt"]
        sys = data["sys"]
        sys_type = sys["type"]
        sys_id = sys["id"]
        sys_country = sys["country"]
        sys_sunrise = sys["country"]
        sys_sunset = sys["sunset"]
        timezone = data["timezone"]
        id = data["id"]
        name = data["name"]
        cod = data["cod"]

        self.data = {
            "api_key": api_key,
            "stadt": stadt,
            "link": url,
            "data": data,
            "koordinaten": coord,
            "wetterr": weather,
            "wetter_id": weather_id,
            "wetter_name": weather_main,
            "wetter_beschreibung": weather_description,
            "weather_icon": weather_icon,
            "base": base,
            "main": main,
            "temperatur": main_temptemp,
            "temperatur_gefühl": main_feels_like,
            "temperatur_mininal": main_temp_min,
            "temperatur_maximal": main_temp_max,
            "luftdruck": main_pressure,
            "luftfeuchtigkeit": main_humidity,
            "visibility": visibility,
            "wind": wind,
            "windstärke": wind_speed,
            "wind_deg": wind_deg,
            "wolken": clouds,
            "wolken_alles": clouds_all,
            "dt": dt,
            "sys": sys,
            "sys_type": sys_type,
            "sys_id": sys_id,
            "land": sys_country,
            "sonnenaufgang": sys_sunrise,
            "sonnenuntergang": sys_sunset,
            "zeitzone": timezone,
            "id": id,
            "name": name,
            "cod": cod
        }

    def get(self, name, stadt=None):
        if stadt:
            try:
                self.init(stadt)
            except:
                return None
        try:
            x = self.data(name)
            return x
        except:
            return None
        if name == "alles":
            return self.data

data = data()
