## API Endpoints

### List all Movies

**GET /movies/**

    {
    "id": 1,
    "name": "Inception",
    "img": "http://example.com/media/images/inception.jpg",
    "summary": "A skilled thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O."
    },
    {
    "id": 2,
    "name": "The Matrix",
    "img": "http://example.com/media/images/the_matrix.jpg",
    "summary": "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers."
    }

### Retrieve a Single Movie

**GET /movies/{id}/**

    {
    "id": 1,
    "name": "Inception",
    "img": "http://example.com/media/images/inception.jpg",
    "summary": "A skilled thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O."
    }

### Create a New Movie

**POST /movies/**

    {
    "name": "Interstellar",
    "img": "http://example.com/media/images/interstellar.jpg",
    "summary": "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival."
    }


    {
    "id": 3,
    "name": "Interstellar",
    "img": "http://example.com/media/images/interstellar.jpg",
    "summary": "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival."
    }

### Update an Existing Movie

**PUT /movies/{id}/**

    {
    "name": "Inception",
    "img": "http://example.com/media/images/inception_updated.jpg",
    "summary": "A skilled thief is given the task of planting an idea into the mind of a C.E.O. using dream-sharing technology."
    }


    {
    "id": 1,
    "name": "Inception",
    "img": "http://example.com/media/images/inception_updated.jpg",
    "summary": "A skilled thief is given the task of planting an idea into the mind of a C.E.O. using dream-sharing technology."
    }

### Partially Update an Existing Movie

**PATCH /movies/{id}/**

    {
    "summary": "A skilled thief uses dream-sharing technology to plant an idea into the mind of a C.E.O."
    }


    {
    "id": 1,
    "name": "Inception",
    "img": "http://example.com/media/images/inception.jpg",
    "summary": "A skilled thief uses dream-sharing technology to plant an idea into the mind of a C.E.O."
    }

### Delete a Movie

**DELETE /movies/{id}/**

No JSON data is required for the DELETE request. You just need to make a DELETE request to the specific movie's URL.
