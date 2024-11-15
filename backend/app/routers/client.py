from fastapi import APIRouter, status

router = APIRouter()

@router.get("/", tags=['client'], status_code=status.HTTP_200_OK)
async def healthCheck():
    return {"message": "API OK"}

@router.get("/get-original-response", tags=['client'], status_code=status.HTTP_200_OK)
async def getOriginalResponse(request: str):

    # TODO: call LLM and return the raw response
    return "Placeholder " + request

@router.get("/get-jailbroken-response", tags=['client'], status_code=status.HTTP_200_OK)
async def getJailbrokenResponse(request: str):
    # TODO: transform request to jailbroken request

    # TODO: call LLM with jailbroken request

    # TODO: return jailbroken response
    return "Jailbreak placeholder " + request
