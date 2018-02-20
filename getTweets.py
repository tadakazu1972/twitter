#------繰り返しTweetデータを取得する
sid = -1
mid = -1
count = 0

res = None
while(True):
    try:
        count = count + 1
        sys.stdout.write("%d, "% count)
        res = getTweetData(u'大阪市', max_id=mid, since_id=sid)
        if res['result']==False:
            #失敗したら終了
            print "status_code", res['status_code']
            break

        if int(res['limit']) == 0:
            # 日付の列'created_datetime'付加
            print "Adding created_at field."
            for d in tweetdata.find({'created_datetime':{ "$exists": False }},{'_id':1, 'created_at':1}):
                #print str_to_date_jp(d['created_at'])
                tweetdata.update({'_id' : d['_id']},{'$set' : {'created_datetime' : str_to_date_jp(d['created_at'])}})
        
