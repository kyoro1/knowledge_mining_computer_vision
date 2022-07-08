In generating `config.ini`, please refer the following template, and put it in this directory.

```config.ini
[Azure]
subscription_key = AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
cv_endpoint = https://cv-kyiwasak.cognitiveservices.azure.com/
language = ja
```

| variables        | description                                                            |
| ---------------- | ---------------------------------------------------------------------- |
| subscription_key | Azure subscription                                                     |
| cv_endpoint      | Rest Endpoint URL provided by Azure Computer Vision                    |
| language[^1]     | Used for the language specifying the language in Azure Computer Vision |

[^1]: In selecting language, refer to [this site](https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/language-support#image-analysis)