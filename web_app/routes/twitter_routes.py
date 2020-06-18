# web_app/routes/twitter_routes.py

from flask import Blueprint, request, render_template, jsonify
from web_app.models import db, User, Tweet #, parse_records
from web_app.services.twitter_service import api as twitter_api_client
from web_app.services.basilica_service import connection as basilica_api_client

twitter_routes = Blueprint("twitter_routes", __name__)

@twitter_routes.route("/users/<screen_name>/fetch")
def fetch_user(screen_name=None):
    print(screen_name)
    # breakpoint()

    # FETCH DATA FROM TWITTER API
    twitter_user = twitter_api_client.get_user(screen_name)
    # tweets = twitter_api_client.user_timeline(screen_name, tweet_mode="extended", count=150, exclude_replies=True, include_rts=False)
    # print("TWEETS COUNT:", len(tweets))
    #return jsonify({"user": user._json, "tweets": [s._json for s in statuses]})

    # STORE TWITTER DATA IN DB

    # get existing user from the db or initialize a new one:
    db_user = User.query.get(twitter_user.id) or User(id=twitter_user.id)
    db_user.screen_name = twitter_user.screen_name
    db_user.name = twitter_user.name
    db_user.location = twitter_user.location
    db_user.followers_count = twitter_user.followers_count
    db.session.add(db_user)
    db.session.commit()
    #return "OK"
    #breakpoint()

    # FETCH TWEETS
    tweets = twitter_api_client.user_timeline(screen_name, tweet_mode="extended", count=150, exclude_replies=True, include_rts=False)
    print("TWEETS COUNT:", len(tweets))
    


    # basilica_api = basilica_api_client()

    all_tweet_texts = [status.full_text for status in tweets]
    embeddings = list(basilica_api_client.embed_sentences(all_tweet_texts, model="twitter"))
    print("NUMBER OF EMBEDDINGS", len(embeddings))

    # # TODO: explore using the zip() function maybe...
    # counter = 0
    for index, status in enumerate(tweets):
        print(index)
        print(status.full_text)
        print("----")
        # embedding = basilica_api_client.embed_sentence(status.full_text, model="twitter") # todo: prefer to make a single request to basilica with all the tweet texts, instead of a request per tweet
        # print(len(embedding))
        embedding = embeddings[index]

        #print(dir(status))
        # get existing tweet from the db or initialize a new one:
        db_tweet = Tweet.query.get(status.id) or Tweet(id=status.id)
        db_tweet.user_id = status.author.id # or db_user.id
        db_tweet.full_text = status.full_text
        db_tweet.embedding = embedding
        db.session.add(db_tweet)
        # counter+=1
    db.session.commit()
    # return "OK"
    print('path A')
    return render_template("user.html", user=db_user, tweets=tweets) # tweets=db_tweets

@twitter_routes.route('/users/new')
def new_user():
    return render_template("new_user.html")

@twitter_routes.route("/users/create", methods=["POST"])
def add_user():
    print("FORM DATA:", dict(request.form))
    screen_name = request.form["screen_name"]
    fetch_user(screen_name)
    # fetch_user(request.form["screen_name"])

    # new_user = User(title=request.form["screen_name"], author_id=request.form["author_name"])
    # db.session.add(new_book)
    # db.session.commit()

    # return jsonify({
    #     "message": "BOOK CREATED OK (TODO)",
    #     "book": dict(request.form)
    # })
    # flash(f"Book '{new_book.title}' created successfully!", "success")
    # return redirect(f"/books")
    print('path B')

    return render_template("user.html", screen_name=screen_name) # tweets=db_tweets
