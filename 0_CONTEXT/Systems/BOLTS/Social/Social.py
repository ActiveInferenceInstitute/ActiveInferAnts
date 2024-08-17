import numpy as np
from typing import Dict, List, Union
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from nltk.sentiment import SentimentIntensityAnalyzer
from networkx import Graph, centrality
from sklearn.feature_extraction.text import TfidfVectorizer
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima.model import ARIMA

class SocialAIC:
    def __init__(self):
        self.sentiment_analyzer = SentimentIntensityAnalyzer()
        self.tfidf_vectorizer = TfidfVectorizer()

    def analyze_social_media_sentiment(self, posts: List[str]) -> List[float]:
        """
        Analyze sentiment of social media posts.

        Args:
            posts (List[str]): List of social media posts.

        Returns:
            List[float]: List of sentiment scores for each post.
        """
        return [self.sentiment_analyzer.polarity_scores(post)['compound'] for post in posts]

    def identify_conflicting_posts(self, posts: List[str], sentiments: List[float], threshold: float) -> List[str]:
        """
        Identify posts with sentiment below a given threshold.

        Args:
            posts (List[str]): List of social media posts.
            sentiments (List[float]): List of sentiment scores corresponding to posts.
            threshold (float): Sentiment threshold for identifying conflicting posts.

        Returns:
            List[str]: List of posts identified as conflicting.
        """
        return [post for post, sentiment in zip(posts, sentiments) if sentiment < threshold]

    def cluster_topics(self, posts: List[str], n_clusters: int) -> Dict[str, List[str]]:
        """
        Perform topic clustering on posts.

        Args:
            posts (List[str]): List of social media posts.
            n_clusters (int): Number of clusters to form.

        Returns:
            Dict[str, List[str]]: Dictionary of cluster topics and their associated posts.
        """
        tfidf_matrix = self.tfidf_vectorizer.fit_transform(posts)
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        cluster_labels = kmeans.fit_predict(tfidf_matrix)
        
        clusters = {f"Cluster_{i}": [] for i in range(n_clusters)}
        for post, label in zip(posts, cluster_labels):
            clusters[f"Cluster_{label}"].append(post)
        
        return clusters

    def calculate_user_involvement(self, users: List[str], sentiments: List[float], threshold: float) -> List[str]:
        """
        Identify users involved in conflicting posts.

        Args:
            users (List[str]): List of user identifiers.
            sentiments (List[float]): List of sentiment scores corresponding to users' posts.
            threshold (float): Sentiment threshold for identifying involved users.

        Returns:
            List[str]: List of users involved in conflicting posts.
        """
        return list(set(user for user, sentiment in zip(users, sentiments) if sentiment < threshold))

    def build_interaction_graph(self, interactions: List[List[int]]) -> Graph:
        """
        Build a graph of user interactions.

        Args:
            interactions (List[List[int]]): List of user interaction pairs.

        Returns:
            Graph: Completed interaction graph.
        """
        graph = Graph()
        graph.add_edges_from(interactions)
        return graph

    def identify_key_influencers(self, graph: Graph, top_n: int) -> List[int]:
        """
        Identify key influencers in the interaction graph.

        Args:
            graph (Graph): User interaction graph.
            top_n (int): Number of top influencers to identify.

        Returns:
            List[int]: List of top N influencers.
        """
        centrality_scores = centrality.eigenvector_centrality(graph)
        return sorted(centrality_scores, key=centrality_scores.get, reverse=True)[:top_n]

    def calculate_post_popularity(self, posts: List[str], interactions: List[List[int]]) -> List[float]:
        """
        Calculate popularity score for each post.

        Args:
            posts (List[str]): List of social media posts.
            interactions (List[List[int]]): List of user interaction pairs.

        Returns:
            List[float]: List of popularity scores for each post.
        """
        interaction_count = {i: 0 for i in range(len(posts))}
        for interaction in interactions:
            interaction_count[interaction[1]] += 1
        return [interaction_count.get(i, 0) for i in range(len(posts))]

    def suggest_engagement_strategies(self, influencers: List[int], popular_topics: List[str]) -> List[str]:
        """
        Suggest engagement strategies based on influencers and popular topics.

        Args:
            influencers (List[int]): List of key influencers.
            popular_topics (List[str]): List of popular topics.

        Returns:
            List[str]: List of suggested engagement strategies.
        """
        strategies = [
            f"Collaborate with influencer {influencer} on topic '{topic}'"
            for influencer, topic in zip(influencers[:3], popular_topics[:3])
        ]
        strategies.append("Organize a panel discussion featuring top influencers")
        strategies.append("Create content series around most popular topics")
        return strategies

    def cluster_employees(self, feedback_sentiments: List[float], interaction_strength: List[float]) -> List[int]:
        """
        Cluster employees based on feedback sentiment and interaction strength.

        Args:
            feedback_sentiments (List[float]): List of feedback sentiment scores.
            interaction_strength (List[float]): List of interaction strength scores.

        Returns:
            List[int]: List of cluster assignments for each employee.
        """
        features = np.array(list(zip(feedback_sentiments, interaction_strength)))
        scaler = StandardScaler()
        normalized_features = scaler.fit_transform(features)
        
        kmeans = KMeans(n_clusters=3, random_state=42)
        return kmeans.fit_predict(normalized_features).tolist()

    def identify_conflicting_employees(self, clusters: List[int], features: List[List[float]]) -> List[int]:
        """
        Identify employees in the conflict cluster.

        Args:
            clusters (List[int]): List of cluster assignments for each employee.
            features (List[List[float]]): List of feature vectors for each employee.

        Returns:
            List[int]: Indices of employees in the conflict cluster.
        """
        cluster_sentiments = {i: [] for i in set(clusters)}
        for cluster, feature in zip(clusters, features):
            cluster_sentiments[cluster].append(feature[0])  # Assuming sentiment is the first feature
        
        conflict_cluster = min(cluster_sentiments, key=lambda k: np.mean(cluster_sentiments[k]))
        return [i for i, cluster in enumerate(clusters) if cluster == conflict_cluster]

    def calculate_team_cohesion(self, interaction_matrix: List[List[int]]) -> float:
        """
        Calculate team cohesion based on interaction matrix.

        Args:
            interaction_matrix (List[List[int]]): Matrix of interaction counts between employees.

        Returns:
            float: Team cohesion score.
        """
        total_interactions = sum(sum(row) for row in interaction_matrix)
        possible_interactions = len(interaction_matrix) * (len(interaction_matrix) - 1)
        return total_interactions / possible_interactions if possible_interactions > 0 else 0

    def suggest_conflict_resolution_strategies(self, conflict_intensity: float, team_cohesion: float) -> List[str]:
        """
        Suggest conflict resolution strategies based on conflict intensity and team cohesion.

        Args:
            conflict_intensity (float): Measure of conflict intensity.
            team_cohesion (float): Measure of team cohesion.

        Returns:
            List[str]: List of suggested conflict resolution strategies.
        """
        strategies = []
        if conflict_intensity > 0.7:
            strategies.append("Implement immediate mediation sessions")
        elif conflict_intensity > 0.4:
            strategies.append("Organize team-building exercises")
        
        if team_cohesion < 0.3:
            strategies.append("Conduct regular team alignment meetings")
        elif team_cohesion < 0.6:
            strategies.append("Encourage cross-functional projects")
        
        strategies.append("Provide conflict resolution training for all team members")
        return strategies

    def decompose_sentiment_time_series(self, sentiments: List[float], timestamps: List[float]) -> Dict[str, List[float]]:
        """
        Decompose sentiment time series into trend, seasonal, and residual components.

        Args:
            sentiments (List[float]): List of sentiment scores.
            timestamps (List[float]): List of corresponding timestamps.

        Returns:
            Dict[str, List[float]]: Dictionary of decomposed components.
        """
        ts = pd.Series(sentiments, index=pd.to_datetime(timestamps, unit='s'))
        result = seasonal_decompose(ts, model='additive', period=7)  # Assuming daily data with weekly seasonality
        return {
            'trend': result.trend.tolist(),
            'seasonal': result.seasonal.tolist(),
            'residual': result.resid.tolist()
        }

    def forecast_sentiment(self, trend: List[float], steps: int) -> List[float]:
        """
        Forecast future sentiment based on trend.

        Args:
            trend (List[float]): List of trend values.
            steps (int): Number of steps to forecast.

        Returns:
            List[float]: List of forecasted values.
        """
        model = ARIMA(trend, order=(1, 1, 1))
        results = model.fit()
        forecast = results.forecast(steps=steps)
        return forecast.tolist()

    def detect_significant_shift(self, forecast: List[float], historical: List[float], threshold: float) -> bool:
        """
        Detect if forecasted sentiment represents a significant shift.

        Args:
            forecast (List[float]): List of forecasted sentiment values.
            historical (List[float]): List of historical sentiment values.
            threshold (float): Threshold for determining significant shift.

        Returns:
            bool: True if a significant shift is detected, False otherwise.
        """
        historical_std = np.std(historical)
        last_historical = historical[-1]
        last_forecast = forecast[-1]
        return abs(last_forecast - last_historical) > threshold * historical_std

    def generate_public_opinion_report(self, current_sentiment: float, trend: List[float], forecast: List[float], volatility: float, shift: bool) -> Dict[str, Union[float, List[float], str]]:
        """
        Generate comprehensive report on public opinion analysis.

        Args:
            current_sentiment (float): Current sentiment score.
            trend (List[float]): List of historical trend values.
            forecast (List[float]): List of forecasted sentiment values.
            volatility (float): Measure of sentiment volatility.
            shift (bool): Indicator of significant shift in sentiment.

        Returns:
            Dict[str, Union[float, List[float], str]]: Comprehensive public opinion report.
        """
        report = {
            'current_sentiment': current_sentiment,
            'historical_trend': trend,
            'forecast': forecast,
            'volatility': volatility,
            'significant_shift': 'Yes' if shift else 'No',
            'summary': f"Current sentiment is {current_sentiment:.2f}. "
                       f"{'A significant shift is expected. ' if shift else 'No significant shift expected. '}"
                       f"Volatility is {'high' if volatility > 0.5 else 'low'} at {volatility:.2f}."
        }
        return report
