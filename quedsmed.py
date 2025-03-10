import requests
import json

AUTHENTICATION_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ODEyMTcsImRpc3BsYXlOYW1lIjoiSG9wIEJ1aSIsImZpcnN0TmFtZSI6IkhvcCIsImxhc3ROYW1lIjoiQnVpIiwidXNlcm5hbWUiOiJ2YW5ob3AzNDk5QGdtYWlsLmNvbSIsImFjY2Vzc0xldmVsIjoic3Vic2NyaWJlciIsInRvY0FjY2VwdGVkIjpmYWxzZSwiZXhwIjoxNzM5NzI0NDM0LCJxYmFua1N1YnNjcmlwdGlvbkVuZERhdGUiOm51bGwsIm9zY2VTdWJzY3JpcHRpb25FbmREYXRlIjpudWxsLCJidW5kbGVTdWJzY3JpcHRpb25FbmREYXRlIjpudWxsLCJhbmF0b215U3Vic2NyaXB0aW9uRW5kRGF0ZSI6bnVsbCwibWVkaWNhbFNjaWVuY2VzU3Vic2NyaXB0aW9uRW5kRGF0ZSI6bnVsbCwiYW5hdG9teUJ1bmRsZVN1YnNjcmlwdGlvbkVuZERhdGUiOm51bGwsIm1yY3BQYXJ0MVN1YnNjcmlwdGlvbkVuZERhdGUiOm51bGwsIm1yY3BQYXJ0MlN1YnNjcmlwdGlvbkVuZERhdGUiOm51bGwsInBhY2VzU3Vic2NyaXB0aW9uRW5kRGF0ZSI6bnVsbCwibXNyYVN1YnNjcmlwdGlvbkVuZERhdGUiOm51bGwsImFuYWVzdGhldGljc0ludGVydmlld1N1YnNjcmlwdGlvbkVuZERhdGUiOm51bGwsImNzdEludGVydmlld1N1YnNjcmlwdGlvbkVuZERhdGUiOm51bGwsImltdEludGVydmlld1N1YnNjcmlwdGlvbkVuZERhdGUiOm51bGwsInJhZGlvbG9neUludGVydmlld1N1YnNjcmlwdGlvbkVuZERhdGUiOm51bGwsInBhZWRpYXRyaWNzSW50ZXJ2aWV3U3Vic2NyaXB0aW9uRW5kRGF0ZSI6bnVsbCwicGxhYjFTdWJzY3JpcHRpb25FbmREYXRlIjpudWxsLCJwbGFiMlN1YnNjcmlwdGlvbkVuZERhdGUiOm51bGwsInZlciI6NCwiaWF0IjoxNzM5MTE5NjM0fQ.40HHggYOPCHRPR30oKj9RnSBNhrEA_3U35pMZ6rJQ_A"
questionId = 28290

# Headers
headers = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9,vi;q=0.8",
    "authorization": f"Bearer {AUTHENTICATION_TOKEN}",
    "content-type": "application/json",
    "priority": "u=1, i",
    "sec-ch-ua": '"Not A(Brand";v="8", "Chromium";v="132", "Microsoft Edge";v="132"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "userapplication": "3",
    "userproduct": "7",
    "Referer": "https://app.quesmed.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
}

# GraphQL query
query = "fragment QuestionUkmlaFields on Question {\n  presentations {\n    id\n    name\n    topicId\n    topic {\n      id\n      name\n      __typename\n    }\n    __typename\n  }\n  conditions {\n    id\n    name\n    topicId\n    topic {\n      id\n      name\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment HighlightFields on HighlightNode {\n  start\n  end\n  text\n  part\n  tag\n  color\n  __typename\n}\n\nfragment QuestionCategoryFields on Question {\n  ... on QuestionSBA {\n    sbaAnswer: answer\n    __typename\n  }\n  ... on QuestionQA {\n    qaAnswer: answer {\n      dose\n      units\n      __typename\n    }\n    __typename\n  }\n  ... on QuestionEMQ {\n    cases {\n      id\n      questionId\n      case\n      explanation\n      label\n      __typename\n    }\n    emqAnswer: answer\n    __typename\n  }\n  ... on QuestionMultiA {\n    multiAnswer: answer\n    __typename\n  }\n  ... on QuestionRanking {\n    rankingAnswer: answer\n    __typename\n  }\n  ... on QuestionSelect3 {\n    select3Answer: answer\n    __typename\n  }\n  ... on QuestionPrescription {\n    prescribeAnswer: answer {\n      dose {\n        value\n        label\n        visible\n        __typename\n      }\n      drug {\n        value\n        label\n        visible\n        __typename\n      }\n      route {\n        value\n        label\n        visible\n        __typename\n      }\n      frequency {\n        value\n        label\n        visible\n        __typename\n      }\n      duration {\n        value\n        label\n        visible\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment QuestionCommentFields on QuestionComment {\n  id\n  createdAt\n  comment\n  parentId\n  likes\n  user {\n    id\n    displayName\n    accessLevel\n    __typename\n  }\n  dislikes\n  isLikedByMe\n  questionId\n  replies {\n    id\n    createdAt\n    comment\n    parentId\n    user {\n      id\n      displayName\n      accessLevel\n      __typename\n    }\n    likes\n    dislikes\n    isLikedByMe\n    questionId\n    __typename\n  }\n  __typename\n}\n\nfragment PictureFields on Picture {\n  id\n  createdAt\n  updatedAt\n  name\n  caption\n  path\n  path256\n  path512\n  overlayPath\n  overlayPath256\n  overlayPath512\n  thumbhash\n  index\n  topicId\n  topic {\n    id\n    name\n    typeId\n    __typename\n  }\n  __typename\n}\n\nfragment ChapterFields on Chapter {\n  id\n  explanation\n  typeId\n  pictures {\n    ...PictureFields\n    __typename\n  }\n  highlights {\n    ...HighlightFields\n    __typename\n  }\n  files {\n    id\n    title\n    url\n    videoId\n    conceptId\n    __typename\n  }\n  __typename\n}\n\nfragment VideoFileFields on File {\n  id\n  title\n  url\n  videoId\n  conceptId\n  __typename\n}\n\nfragment VideoFields on Video {\n  id\n  demo\n  status\n  title\n  museId\n  startTime\n  endTime\n  thumbnail\n  live\n  description\n  duration\n  startTime\n  endTime\n  viewsToday\n  views\n  userViewed\n  osceStation {\n    id\n    name\n    hiddenName\n    __typename\n  }\n  concepts {\n    id\n    name\n    __typename\n  }\n  files {\n    ...VideoFileFields\n    __typename\n  }\n  __typename\n}\n\nfragment ConceptFields on Concept {\n  id\n  name\n  demo\n  status\n  typeId\n  entitlement {\n    id\n    name\n    __typename\n  }\n  topicId\n  topic {\n    id\n    name\n    typeId\n    __typename\n  }\n  chapterId\n  chapter {\n    ...ChapterFields\n    __typename\n  }\n  videos {\n    ...VideoFields\n    __typename\n  }\n  userNote {\n    id\n    userId\n    conceptId\n    note\n    updatedAt\n    __typename\n  }\n  userChapter {\n    id\n    userId\n    conceptId\n    explanation\n    updatedAt\n    __typename\n  }\n  __typename\n}\n\nfragment QuestionFields on Question {\n  id\n  conceptId\n  difficulty\n  dislikes\n  explanation\n  learningPoint\n  isLikedByMe\n  userPoint\n  likes\n  question\n  totalVotes\n  typeId\n  psaSectionId\n  highlights {\n    ...HighlightFields\n    __typename\n  }\n  choices {\n    id\n    explanation\n    name\n    label\n    answer\n    votes\n    picture {\n      ...PictureFields\n      __typename\n    }\n    __typename\n  }\n  comments {\n    ...QuestionCommentFields\n    __typename\n  }\n  concept {\n    totalCards\n    ...ConceptFields\n    __typename\n  }\n  pictures {\n    ...PictureFields\n    __typename\n  }\n  ...QuestionUkmlaFields\n  ...QuestionCategoryFields\n  __typename\n}\n\nfragment MarksheetMarkFields on MarksheetMark {\n  id\n  flagged\n  index\n  questionChoiceId\n  marksheetId\n  timeTaken\n  isAnswered\n  striked\n  mark\n  questionId\n  question {\n    ...QuestionFields\n    __typename\n  }\n  __typename\n}\n\nfragment BuilderConfigFields on BuilderConfigData {\n  difficulty\n  isTest\n  numberOfQuestions\n  secondsPerQuestion\n  unseen\n  seenCorrect\n  seenIncorrect\n  __typename\n}\n\nfragment MarksheetFields on Marksheet {\n  id\n  topicConceptData\n  currentMarkId\n  completed\n  passingMark\n  duration\n  timeTaken\n  topicIds\n  topicNames\n  mockTestId\n  totalQuestions\n  solo\n  agoraId\n  sessionId\n  state\n  createdAt\n  startedAt\n  endedAt\n  typeId\n  isTestMarksheet\n  source\n  correct\n  incorrect\n  entitlement {\n    id\n    name\n    __typename\n  }\n  preBuildData {\n    buildRef\n    seenCorrect\n    seenIncorrect\n    unseen\n    __typename\n  }\n  user {\n    id\n    displayName\n    __typename\n  }\n  users {\n    id\n    displayName\n    __typename\n  }\n  activeUsers {\n    id\n    displayName\n    __typename\n  }\n  builderConfig {\n    ...BuilderConfigFields\n    __typename\n  }\n  marks {\n    ...MarksheetMarkFields\n    __typename\n  }\n  __typename\n}\n\nquery Marksheet($id: Int!) {\n  restricted {\n    marksheet(id: $id) {\n      ...MarksheetFields\n      __typename\n    }\n    __typename\n  }\n}"

# Request payload
payload = {
    "operationName": "Marksheet",
    "variables": {"id": questionId},
    "query": query
}

# Make the POST request
url = "https://server.quesmed.com/graphql"
response = requests.post(url, headers=headers, json=payload)

# Handle the response
if response.status_code == 200:
    data = response.json()
    print(json.dumps(data, indent=2))
else:
    print(f"Error: {response.status_code}")
    data = response.json()
    print("data", data)