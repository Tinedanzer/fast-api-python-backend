from fastapi import APIRouter

from app.api.routes import admin, widget, carebear

carebear2='\u0336'.join(' definitelyNotCareBears') + '\u0336'
# for c in 'definitelynotcarebears':
    # carebear2 += c+'\u0336'
print(carebear2)
router = APIRouter()
router.include_router(admin.router, tags=["admin"], prefix="/admin")
router.include_router(widget.router, tags=["widget"], prefix="/widget")
router.include_router(carebear.router, tags=[carebear2+' '+"Traveler_info"], prefix='/'+carebear2 +"/Travelers")
# router.include_router()