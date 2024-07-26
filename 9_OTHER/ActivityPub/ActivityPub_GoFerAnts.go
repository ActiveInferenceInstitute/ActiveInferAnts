package main

import (
	"encoding/json"
	"fmt"
	"math/rand"
	"time"
	"net/http"
	"crypto/rsa"
	"crypto/rand"
	"strings"

	"github.com/go-fed/activity/streams"
	"github.com/go-fed/activity/streams/vocab"
	"github.com/go-fed/httpsig"
)

// Agent represents an active inference agent in the ActivityPub ecosystem
type Agent struct {
	ID            string
	Beliefs       map[string]float64
	Preferences   map[string]float64
	Outbox        []vocab.ActivityStreamsObject
	Inbox         []vocab.ActivityStreamsObject
	Followers     []string
	Following     []string
	PrivateKey    *rsa.PrivateKey
	PublicKey     *rsa.PublicKey
	KeyID         string
	LikedPosts    map[string]bool
	SharedPosts   map[string]bool
}

// Environment represents the ActivityPub environment
type Environment struct {
	Agents []*Agent
	Posts  []vocab.ActivityStreamsNote
}

// CreateAgent initializes a new agent with random beliefs, preferences, and a key pair
func CreateAgent(id string) *Agent {
	privateKey, _ := rsa.GenerateKey(rand.Reader, 2048)
	publicKey := &privateKey.PublicKey
	keyID := fmt.Sprintf("%s#main-key", id)

	return &Agent{
		ID:          id,
		Beliefs:     map[string]float64{"quality": rand.Float64(), "relevance": rand.Float64(), "engagement": rand.Float64()},
		Preferences: map[string]float64{"quality": rand.Float64(), "relevance": rand.Float64(), "engagement": rand.Float64()},
		Outbox:      []vocab.ActivityStreamsObject{},
		Inbox:       []vocab.ActivityStreamsObject{},
		Followers:   []string{},
		Following:   []string{},
		PrivateKey:  privateKey,
		PublicKey:   publicKey,
		KeyID:       keyID,
		LikedPosts:  make(map[string]bool),
		SharedPosts: make(map[string]bool),
	}
}

// CreatePost generates a new ActivityPub Note
func CreatePost(content string, actor string) vocab.ActivityStreamsNote {
	note := streams.NewActivityStreamsNote()
	
	noteContent := streams.NewActivityStreamsContentProperty()
	noteContent.SetXMLSchemaString(content)
	note.SetActivityStreamsContent(noteContent)

	attributedTo := streams.NewActivityStreamsAttributedToProperty()
	attributedTo.AppendIRI(vocab.IRI(actor))
	note.SetActivityStreamsAttributedTo(attributedTo)

	published := streams.NewActivityStreamsPublishedProperty()
	published.Set(time.Now())
	note.SetActivityStreamsPublished(published)

	id := streams.NewJSONLDIdProperty()
	id.Set(vocab.IRI(fmt.Sprintf("%s/notes/%d", actor, time.Now().UnixNano())))
	note.SetJSONLDId(id)

	// Add tags
	tags := extractHashtags(content)
	if len(tags) > 0 {
		tagProperty := streams.NewActivityStreamsTagProperty()
		for _, tag := range tags {
			hashTag := streams.NewActivityStreamsHashtag()
			hashTag.SetActivityStreamsName(streams.NewActivityStreamsNameProperty().AppendXMLSchemaString(tag))
			tagProperty.AppendActivityStreamsHashtag(hashTag)
		}
		note.SetActivityStreamsTag(tagProperty)
	}

	return note
}

// extractHashtags extracts hashtags from the content
func extractHashtags(content string) []string {
	words := strings.Fields(content)
	var hashtags []string
	for _, word := range words {
		if strings.HasPrefix(word, "#") {
			hashtags = append(hashtags, strings.TrimPrefix(word, "#"))
		}
	}
	return hashtags
}

// PerceiveEnvironment updates agent's beliefs based on the environment
func (a *Agent) PerceiveEnvironment(env *Environment) {
	for _, post := range env.Posts {
		content, err := post.GetActivityStreamsContent().GetXMLSchemaString()
		if err != nil {
			continue
		}
		quality := float64(len(content)) / 100 // Simplified quality metric
		relevance := calculateRelevance(content, a.Preferences)
		engagement := calculateEngagement(post)

		a.Beliefs["quality"] = (a.Beliefs["quality"]*0.7 + quality*0.3)
		a.Beliefs["relevance"] = (a.Beliefs["relevance"]*0.7 + relevance*0.3)
		a.Beliefs["engagement"] = (a.Beliefs["engagement"]*0.7 + engagement*0.3)
	}
}

// calculateRelevance calculates the relevance of a post based on agent's preferences
func calculateRelevance(content string, preferences map[string]float64) float64 {
	// Implement a more sophisticated relevance calculation
	// This could involve natural language processing, topic modeling, etc.
	return rand.Float64() // Placeholder implementation
}

// calculateEngagement calculates the engagement level of a post
func calculateEngagement(post vocab.ActivityStreamsNote) float64 {
	// Implement engagement calculation based on likes, shares, comments, etc.
	// This would require additional properties in the Note type
	return rand.Float64() // Placeholder implementation
}

// Act performs an action based on the agent's beliefs and preferences
func (a *Agent) Act(env *Environment) {
	if a.shouldCreatePost() {
		a.createPost(env)
	}
	
	for _, post := range env.Posts {
		if a.shouldLikePost(post) {
			a.likePost(post)
		}
		if a.shouldSharePost(post) {
			a.sharePost(post, env)
		}
	}
	
	if a.shouldFollowNewAgent() {
		a.followRandomAgent(env)
	}
}

func (a *Agent) shouldCreatePost() bool {
	return a.Beliefs["quality"] > 0.6 && a.Beliefs["relevance"] > 0.6 && a.Beliefs["engagement"] > 0.5
}

func (a *Agent) createPost(env *Environment) {
	content := fmt.Sprintf("High quality and relevant content from %s #ActivityPub #AI", a.ID)
	note := CreatePost(content, a.ID)
	
	create := streams.NewActivityStreamsCreate()
	create.SetActivityStreamsObject(streams.NewActivityStreamsObjectProperty().AppendActivityStreamsNote(note))
	create.SetActivityStreamsActor(streams.NewActivityStreamsActorProperty().AppendIRI(vocab.IRI(a.ID)))
	
	to := streams.NewActivityStreamsToProperty()
	for _, follower := range a.Followers {
		to.AppendIRI(vocab.IRI(follower))
	}
	create.SetActivityStreamsTo(to)
	
	a.Outbox = append(a.Outbox, create)
	env.Posts = append(env.Posts, note)
	
	// Distribute to followers
	for _, follower := range a.Followers {
		for _, agent := range env.Agents {
			if agent.ID == follower {
				agent.Inbox = append(agent.Inbox, create)
				break
			}
		}
	}
}

func (a *Agent) shouldLikePost(post vocab.ActivityStreamsNote) bool {
	postID, _ := post.GetJSONLDId().Get()
	_, alreadyLiked := a.LikedPosts[postID.String()]
	return !alreadyLiked && rand.Float64() > 0.7 // 30% chance to like a new post
}

func (a *Agent) likePost(post vocab.ActivityStreamsNote) {
	like := streams.NewActivityStreamsLike()
	like.SetActivityStreamsActor(streams.NewActivityStreamsActorProperty().AppendIRI(vocab.IRI(a.ID)))
	like.SetActivityStreamsObject(streams.NewActivityStreamsObjectProperty().AppendActivityStreamsNote(post))
	
	a.Outbox = append(a.Outbox, like)
	postID, _ := post.GetJSONLDId().Get()
	a.LikedPosts[postID.String()] = true
}

func (a *Agent) shouldSharePost(post vocab.ActivityStreamsNote) bool {
	postID, _ := post.GetJSONLDId().Get()
	_, alreadyShared := a.SharedPosts[postID.String()]
	return !alreadyShared && rand.Float64() > 0.8 // 20% chance to share a new post
}

func (a *Agent) sharePost(post vocab.ActivityStreamsNote, env *Environment) {
	announce := streams.NewActivityStreamsAnnounce()
	announce.SetActivityStreamsActor(streams.NewActivityStreamsActorProperty().AppendIRI(vocab.IRI(a.ID)))
	announce.SetActivityStreamsObject(streams.NewActivityStreamsObjectProperty().AppendActivityStreamsNote(post))
	
	to := streams.NewActivityStreamsToProperty()
	for _, follower := range a.Followers {
		to.AppendIRI(vocab.IRI(follower))
	}
	announce.SetActivityStreamsTo(to)
	
	a.Outbox = append(a.Outbox, announce)
	postID, _ := post.GetJSONLDId().Get()
	a.SharedPosts[postID.String()] = true
	
	// Distribute to followers
	for _, follower := range a.Followers {
		for _, agent := range env.Agents {
			if agent.ID == follower {
				agent.Inbox = append(agent.Inbox, announce)
				break
			}
		}
	}
}

func (a *Agent) shouldFollowNewAgent() bool {
	return len(a.Following) < 10 && rand.Float64() > 0.9 // 10% chance to follow a new agent if following less than 10
}

func (a *Agent) followRandomAgent(env *Environment) {
	if len(env.Agents) <= 1 {
		return
	}
	
	var targetAgent *Agent
	for targetAgent == nil || targetAgent.ID == a.ID {
		targetAgent = env.Agents[rand.Intn(len(env.Agents))]
	}
	
	a.Follow(targetAgent)
}

// Follow makes the agent follow another agent
func (a *Agent) Follow(target *Agent) {
	follow := streams.NewActivityStreamsFollow()
	follow.SetActivityStreamsActor(streams.NewActivityStreamsActorProperty().AppendIRI(vocab.IRI(a.ID)))
	follow.SetActivityStreamsObject(streams.NewActivityStreamsObjectProperty().AppendIRI(vocab.IRI(target.ID)))
	
	a.Outbox = append(a.Outbox, follow)
	target.Inbox = append(target.Inbox, follow)
	
	a.Following = append(a.Following, target.ID)
	target.Followers = append(target.Followers, a.ID)
}

// SignRequest signs an HTTP request using HTTP Signatures
func (a *Agent) SignRequest(req *http.Request) error {
	signer, _, err := httpsig.NewSigner(
		[]httpsig.Algorithm{httpsig.RSA_SHA256},
		httpsig.DigestSha256,
		[]string{httpsig.RequestTarget, "date", "digest"},
		httpsig.Signature,
		0,
	)
	if err != nil {
		return err
	}

	return signer.SignRequest(a.PrivateKey, a.KeyID, req, nil)
}

// RunSimulation executes the active inference simulation
func RunSimulation(numAgents, numIterations int) {
	env := &Environment{}

	for i := 0; i < numAgents; i++ {
		agent := CreateAgent(fmt.Sprintf("https://example.com/users/agent%d", i))
		env.Agents = append(env.Agents, agent)
	}

	// Create a more complex follow network
	for i, agent := range env.Agents {
		numFollows := rand.Intn(numAgents / 2)
		for j := 0; j < numFollows; j++ {
			targetIndex := (i + j + 1) % numAgents
			agent.Follow(env.Agents[targetIndex])
		}
	}

	for i := 0; i < numIterations; i++ {
		for _, agent := range env.Agents {
			agent.PerceiveEnvironment(env)
			agent.Act(env)
		}
	}

	// Print simulation results
	fmt.Printf("Simulation completed with %d agents and %d iterations\n", numAgents, numIterations)
	fmt.Printf("Total posts created: %d\n", len(env.Posts))

	// Print the last 5 posts or all if less than 5
	numPostsToPrint := min(5, len(env.Posts))
	fmt.Printf("Last %d posts:\n", numPostsToPrint)
	for i := len(env.Posts) - numPostsToPrint; i < len(env.Posts); i++ {
		content, _ := env.Posts[i].GetActivityStreamsContent().GetXMLSchemaString()
		attributedTo := env.Posts[i].GetActivityStreamsAttributedTo().Begin().GetIRI().String()
		postJSON, _ := json.MarshalIndent(env.Posts[i], "", "  ")
		fmt.Printf("Post %d:\nContent: %s\nAttributed to: %s\nFull ActivityPub Note:\n%s\n\n", i+1, content, attributedTo, string(postJSON))
	}

	// Print agent statistics
	for _, agent := range env.Agents {
		fmt.Printf("Agent %s:\n", agent.ID)
		fmt.Printf("  Followers: %d\n", len(agent.Followers))
		fmt.Printf("  Following: %d\n", len(agent.Following))
		fmt.Printf("  Outbox size: %d\n", len(agent.Outbox))
		fmt.Printf("  Inbox size: %d\n", len(agent.Inbox))
		fmt.Printf("  Liked posts: %d\n", len(agent.LikedPosts))
		fmt.Printf("  Shared posts: %d\n", len(agent.SharedPosts))
		fmt.Printf("  Key ID: %s\n\n", agent.KeyID)
	}
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {
	rand.Seed(time.Now().UnixNano())
	RunSimulation(10, 20)
}
