class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.posts = []

    def create_post(self, content):
        post = Post(content, self)
        self.posts.append(post)
        return post

    def upvote(self, post):
        post.upvotes += 1

    def downvote(self, post):
        post.downvotes += 1


class Post:
    def __init__(self, content, author):
        self.content = content
        self.author = author
        self.upvotes = 0
        self.downvotes = 0
        self.replies = []

    def add_reply(self, content, author):
        reply = Reply(content, author)
        self.replies.append(reply)
        return reply

    def calculate_score(self):
        return self.upvotes - self.downvotes


class Reply:
    def __init__(self, content, author):
        self.content = content
        self.author = author
        self.upvotes = 0
        self.downvotes = 0
        self.is_private = False
        self.reactions = []

    def make_private(self):
        self.is_private = True

    def add_reaction(self, reaction_type, user):
        reaction = Reaction(reaction_type, user)
        self.reactions.append(reaction)


class Reaction:
    def __init__(self, reaction_type, user):
        self.reaction_type = reaction_type
        self.user = user


# Example usage:
# Create some users
alice = User("AliceExample", "alicepassword")
bob = User("BobExample", "bobpassword")

# Alice creates a post
post_by_alice = alice.create_post("How does OOD work in Python?")

# Bob replies to Alice's post
reply_by_bob = post_by_alice.add_reply(
    "OOD in Python works through classes and objects.", bob)

# Alice upvotes Bob's reply
alice.upvote(reply_by_bob)

# Bob marks his reply as private
reply_by_bob.make_private()

# Checking if the reply is private and the score
print(f"Bob's Reply Private: {reply_by_bob.is_private}")
print(f"Bob's Reply Score: {reply_by_bob.upvotes - reply_by_bob.downvotes}")
