from fastapi import APIRouter, status, Query
from fastapi.responses import JSONResponse
from elastic import es
from app.additional_functions import aggregate,aggregate_all
from typing import Optional


router = APIRouter(tags=['Search'])


@router.post('/search/main', status_code=200)
def search(request: str):
    body = {
            "query": {
                "multi_match":
                    {
                        "query": request,
                        "fields": ['title', 'username','tags']
                    }
            }
    }
    res = es.search(index=['courses', 'lessons', 'posts', 'users'], body=body)
    print(res)
    return JSONResponse(
        status_code=status.HTTP_200_OK, content=aggregate_all(res['hits']['hits']))


@router.post('/search/courses', status_code=200)
def search_courses(request: str, page: Optional[int] = Query(1), size: Optional[int] = Query(10)):
    body = {
        "from": (page-1)*size,
        "size": size,
        "query": {
            "multi_match":
                {
                    "query": request,
                    "fields": ['title']
                }
        }
    }
    res = es.search(index=['courses'], body=body)
    count = es.count(index=['courses'])['count']

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=aggregate(res['hits']['hits'],page,size,count))


@router.post('/search/lessons', status_code=200)
def search_lessons(request: str, page: Optional[int] = Query(1), size: Optional[int] = Query(10)):
    body = {
        "from": (page - 1) * size,
        "size": size,
        "query":
            {
                "multi_match":
                    {
                        "query": request,
                        "fields": ['title','tags']
                    }
            }
    }
    res = es.search(index=['lessons'], body=body)
    count = es.count(index=['lessons'])['count']
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=aggregate(res['hits']['hits'], page, size, count))


@router.post('/search/posts', status_code=200)
def search_posts(request: str, page: Optional[int] = Query(1), size: Optional[int] = Query(10)):
    body = {
        "from": (page - 1) * size,
        "size": size,
        "query": {
            "multi_match": {
                "query": request,
                "fields": ['title']
            }
        }
    }
    res = es.search(index=['posts'], body=body)
    count = es.count(index=['posts'])['count']
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=aggregate(res['hits']['hits'], page, size, count))


@router.post('/search/users', status_code=200)
def search_users(request: str, page: Optional[int] = Query(1), size: Optional[int] = Query(10)):
    body = {
        "from": (page - 1) * size,
        "size": size,
        "query":
            {
            "multi_match":
                {
                "query": request,
                "fields": ['username']
                }
            }
    }
    res = es.search(index=['users'], body=body)
    count = es.count(index=['users'])['count']
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=aggregate(res['hits']['hits'], page, size, count))
