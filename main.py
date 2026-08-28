from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.weather import router as weather_router
from routes.alerts import router as alerts_router
from routes.location import router as location_router
app=FastAPI(title='WeatherGPT - Rohit Backend Demo',version='1.0.0')
app.add_middleware(CORSMiddleware,allow_origins=['*'],allow_credentials=True,allow_methods=['*'],allow_headers=['*'])
app.include_router(weather_router,prefix='/api'); app.include_router(alerts_router,prefix='/api'); app.include_router(location_router,prefix='/api')
@app.get('/')
def home(): return {'message':'WeatherGPT Backend is running','status':'online'}
@app.get('/health')
def health(): return {'status':'healthy'}
