from omdbapi.movie_search import GetMovie
from fastapi import FastAPI, HTTPException, status

app = FastAPI()


@app.get("/find_by_movie-name/{movieName}", status_code=status.HTTP_200_OK)
async def getMovieByName(movieName: str):
    movie = GetMovie(api_key='a098f2f5')
    try:
        return movie.get_movie(title=movieName)
    except:
        raise HTTPException(status_code=404, detail="Movie not found")
