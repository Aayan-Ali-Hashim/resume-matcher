from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_similarity_score(resume, jd):
    tfidf = TfidfVectorizer()
    vectors = tfidf.fit_transform([resume, jd])
    score = cosine_similarity(vectors[0:1], vectors[1:])
    return round(score[0][0] * 100, 2)
