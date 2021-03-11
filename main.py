"""
What's the weather like in there?
OpenWeatherMap API를 활용하여 세계 특 5가지 도시의 날씨를 알려주는 프로그램.
멋쟁이 사자처럼 "[심화] 같이 푸는 PYTHON" 강좌 참조

"""
import requests
import json

print("1. 서울, 2. 토론토, 3. 밴쿠버, 4. 런던, 5. 맨체스터, 6. 도쿄, 7. 뉴욕")
city_list = ["Seoul", "Toronto", "Vancouver", "London", "Manchester", "Tokyo", "New York"]
city_code = int(input("어떤 도시의 날씨가 알고싶나요?: "))
city = city_list[city_code-1]

apikey = "##############################3"
lang = "kr"

api = f"http://api.openweathermap.org/data/2.5/" \
      f"weather?q={city}&appid={apikey}&lang={lang}&units=metric"     # f-string

result = requests.get(api)
# print(result.text)

data = json.loads(result.text)

city_kr = ["서울", "토론토", "밴쿠버", "런던", "맨체스터", "도쿄", "뉴욕"]

# 지역 : 한글 도시명
print(city_kr[city_code-1], "의 날씨입니다.")
# 자세한 날씨 : weather - description
print("날씨는 ", data["weather"][0]["description"], "입니다.")
# 현재 온도 : main - temp
print("현재 온도는 ", data["main"]["temp"], "°C 입니다.")
# 체감 온도 : main - feels_like
print("하지만 체감 온도는 ", data["main"]["feels_like"], "°C 입니다.")
# 최저 기온 : main - temp_min
print("최저 기온은 ", data["main"]["temp_min"], "°C 입니다.")
# 최고 기온 : main - temp_max
print("최고 기온은 ", data["main"]["temp_max"], "°C 입니다.")
# 습도 : main - humidity
print("습도는 ", data["main"]["humidity"], "입니다.")
# 기압 : main - pressure
print("기압은 ", data["main"]["pressure"], "입니다.")
# 풍향 : wind - deg
print("풍향은 ", data["wind"]["deg"], "입니다.")
# 풍속 : wind - speed
print("풍속은 ", data["wind"]["speed"], "입니다.")
