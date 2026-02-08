
# REST – Clean Concept Notes

These notes summarize the key REST concepts discussed, with intuition, examples, and interview-ready definitions.

---

## What is REST?

**REST (Representational State Transfer)** is an architectural style for designing APIs.

> REST defines *how* clients interact with resources over HTTP using a consistent, predictable interface.

REST is not a framework or library — it’s a **set of constraints**.

---

## REST is Resource-Based

### What is a Resource?

A **resource** is any *thing* your system exposes:

* User
* Movie / WatchList
* Review
* Order

Usually, a resource maps to a **database model**.

---

### What “resource-based” means

* URLs represent **nouns (things)**
* Actions are expressed using **HTTP methods**, not URL names

#### ❌ Not RESTful (action-based)

```
POST /createReview
POST /deleteMovie
```

#### ✅ RESTful (resource-based)

```
POST   /movies/3/reviews/
GET    /movies/3/reviews/
DELETE /movies/3/
```

**Mental model:**

```
URL    = WHAT (resource)
Method = HOW (action)
```

---

### Same URL, different behavior

```
GET    /reviews/5/   → fetch review
PUT    /reviews/5/   → update review
DELETE /reviews/5/   → delete review
```

The URL does not change — the HTTP method does.

---

## Nested Resources

REST allows expressing **relationships** naturally using URLs.

Example:

```
/reviews/                  → all reviews
/watchlists/3/reviews/     → reviews for watchlist with id=3
```

This maps directly to database relations:

```
Review → ForeignKey → WatchList
```

---

## REST is Stateless

### What “stateless” means

> The server does **not remember client state** between requests.

Each request is:

* independent
* self-contained
* complete on its own

---

### What the server does NOT store

* login sessions
* previous requests
* user navigation history

Unless the request itself sends the information.

---

### Every request must carry all context

Example:

```
GET /reviews/
Authorization: Bearer <JWT>
```

The server does not say:

> “I remember this user from earlier.”

It verifies the token **again** for every request.

---

### Stateless vs Stateful (contrast)

#### ❌ Stateful (traditional sessions)

* Server stores session data
* Session ID maps to user info
* Harder to scale

#### ✅ Stateless (REST)

* Client stores token (JWT / API key)
* Token sent with every request
* Server verifies, stores nothing

---

### Why statelessness matters

1. **Scalability** – any request can go to any server
2. **Reliability** – no session loss on crash
3. **Simplicity** – easier debugging and caching

---

### JWT and Statelessness

Even though JWT contains data:

* JWT is stored on the **client**
* Server only verifies signature
* No client state stored server-side

REST remains stateless.

---

## REST and APIs (clarifying the idea)

An API is **not just URLs**.

An API is a **contract** defining:

* endpoints (URLs)
* HTTP methods
* request/response formats (JSON)
* validation rules
* status codes

Clients talk to endpoints — **endpoints do not talk to each other**.

```
Client → API Endpoint → Database
```

---

## REST vs Other API Styles (high level)

* REST → resource-based, stateless
* GraphQL → query-based, client controls data shape
* gRPC → RPC-style, high performance, binary
* WebSockets → stateful, real-time
* SOAP → XML-based, legacy enterprise

---

## Interview-Ready One-Liners

* **REST (definition):**

  > REST is an architectural style where resources are identified by URLs and manipulated using standard HTTP methods.

* **Resource-based:**

  > REST is resource-based because URLs represent resources, not actions, and HTTP methods define behavior.

* **Statelessness:**

  > REST is stateless because each request contains all the information required, and the server does not store client context.

---

## Key Mental Models (Lock These In)

* Resource = noun
* Method = verb
* URL describes *data*, not *behavior*
* Server remembers nothing between requests
* Client sends full context every time

---

## Final Note

If you see:

* verbs in URLs ❌
* server sessions in APIs ❌
* hidden dependency on previous requests ❌

…it’s not truly RESTful.

---

These notes are meant to be **revisited**, not memorized. Understanding these ideas deeply helps with backend design, system design, and interviews.


## Lecture no. 31: Viewsets and Routers
In viewsets, we combine the logic of list and detail. Means we can combine the two URLS and views and using router we can handle everything.

We will use this step for stream-list and stream-detail.

Routers helps us to combine any type of links.

Basically we try to short the code.
Mostly useful for complete list and then for a single instance. 
and custom urls using routers is a lot complex not recommended.

Use generic URLs because they are simple.

## Lecture no. 32: ModelViewSets

with viewsets, we were adding manually CRUD ops, but using ModelViewSets, we don't need to add these manually. All these things are inherited from mixins.


