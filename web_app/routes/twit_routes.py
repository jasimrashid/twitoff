# web_app/routes/twit_routes.py

from flask import Blueprint, jsonify, request, render_template #, flash, redirect

from web_app.models import Tweet, db, parse_records
twit_routes = Blueprint("twit_routes", __name__)

@twit_routes.route("/tweets.json")
def list_tweets():
    # tweets = [
    #     {"id": 1, "text": "Tweet 1"},
    #     {"id": 2, "text": "Tweet 2"},
    #     {"id": 3, "text": "Tweet 3"},
    # ]
    tweet_records = Tweet.query.all()
    print(tweet_records)
    tweets = parse_records(tweet_records)
    return jsonify(tweets)

@twit_routes.route("/tweets")
def list_tweets_for_humans():
    # tweets = [
    #     {"id": 1, "text": "Tweet 1"},
    #     {"id": 2, "text": "Tweet 2"},
    #     {"id": 3, "text": "Tweet 3"},
    # ]
    # breakpoint()
    print("hello")
    tweet_records = Tweet.query.all()
    # print(tweet_records)
    tweets = parse_records(tweet_records)
    return render_template("tweets.html", message="Here's some tweets", tweets=tweets)

@twit_routes.route("/tweets/new")
def new_user():
    return render_template("new_user.html")

@twit_routes.route("/tweets/create", methods=["POST"])
def add_user():
    print("FORM DATA:", dict(request.form))

    # breakpoint()

    new_tweet = Tweet(text=request.form["text"], user=request.form["user"])
    db.session.add(new_tweet)
    db.session.commit()

    return jsonify({
        "message": "TWEET CREATED OK (TODO)",
        "text": dict(request.form)
    })
    # flash(f"Tweet '{new_tweet.title}' created successfully!", "success")
    # return redirect(f"/tweets")
