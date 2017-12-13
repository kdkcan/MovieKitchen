from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests
from numpy import matrix
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.dates import DateFormatter
import datetime
import random


@csrf_exempt
def index(request):
    if request.method == "POST":

        slider1 = request.POST.get("slider1", "")

        if slider1 == "-3":
            slider1 = (1.0 / 7.0),
        if slider1 == "-2":
            slider1 = (1.0 / 5.0)
        if slider1 == "-1":
            slider1 = (1.0 / 3.0)
        if slider1 == "0":
            slider1 = 1.0
        if slider1 == "1":
            slider1 = 3.0
        if slider1 == "2":
            slider1 = 5.0
        if slider1 == "3":
            slider1 = 7.0


        slider2 = request.POST.get("slider2", "")

        if slider2 == "-3":
            slider2 = (1.0 / 7.0)
        if slider2 == "-2":
            slider2 = (1.0 / 5.0)
        if slider2 == "-1":
            slider2 = (1.0 / 3.0)
        if slider2 == "0":
            slider2 = 1.0
        if slider2 == "1":
            slider2 = 3.0
        if slider2 == "2":
            slider2 = 5.0
        if slider2 == "3":
            slider2 = 7.0

        slider3 = request.POST.get("slider3", "")

        if slider3 == "-3":
            slider3 = (1.0 / 7.0)
        if slider3 == "-2":
            slider3 = (1.0 / 5.0)
        if slider3 == "-1":
            slider3 = (1.0 / 3.0)
        if slider3 == "0":
            slider3 = 1.0
        if slider3 == "1":
            slider3 = 3.0
        if slider3 == "2":
            slider3 = 5.0
        if slider3 == "3":
            slider3 = 7.0

        subSlider = request.POST.get("subSlider", "")

        if subSlider == "-3":
            subSlider = (1.0 / 7.0)
        if slider1 == "-2":
            subSlider = (1.0 / 5.0)
        if subSlider == "-1":
            subSlider = (1.0 / 3.0)
        if subSlider == "0":
            subSlider = 1.0
        if subSlider == "1":
            subSlider = 3.0
        if subSlider == "2":
            subSlider = 5.0
        if subSlider == "3":
            subSlider = 7.0

        act1_t1 = request.POST.get("act1_t1", "")
        act1_t1tid = request.POST.get("act1_t1tid", "")
        act2_t1 = request.POST.get("act2_t1", "")
        act2_t1tid = request.POST.get("act2_t1tid", "")
        act3_t1 = request.POST.get("act3_t1", "")
        act3_t1tid = request.POST.get("act3_t1tid", "")
        d_t1 = request.POST.get("d_t1", "")
        s_t1 = request.POST.get("s_t1", "")
        b_t1 = request.POST.get("b_t1", "")


        act1_t2 = request.POST.get("act1_t2", "")
        act1_t2tid = request.POST.get("act1_t2tid", "")
        act2_t2 = request.POST.get("act2_t2", "")
        act2_t2tid = request.POST.get("act2_t2tid", "")
        act3_t2 = request.POST.get("act3_t2", "")
        act3_t2tid = request.POST.get("act3_t2tid", "")
        d_t2 = request.POST.get("d_t2", "")
        s_t2 = request.POST.get("s_t2", "")
        b_t2 = request.POST.get("b_t2", "")

        act1_t3 = request.POST.get("act1_t3", "")
        act1_t3tid = request.POST.get("act1_t3tid", "")
        act2_t3 = request.POST.get("act2_t3", "")
        act2_t3tid = request.POST.get("act2_t3tid", "")
        act3_t3 = request.POST.get("act3_t3", "")
        act3_t3tid = request.POST.get("act3_t3tid", "")
        d_t3 = request.POST.get("d_t3", "")
        s_t3 = request.POST.get("s_t3", "")
        b_t3 = request.POST.get("b_t3", "")

        try:
            response1 = requests.get(
                "http://api.tmdb.org/3/search/person?api_key=580966185e2883c73da7ba529a4ac3fe&query=" + act1_t1)
            data = response1.json()
            act1_t1Port = (data["results"][0]["popularity"])
            act1_t1Port = float(act1_t1Port)

            response2 = requests.get(
                "http://api.tmdb.org/3/search/person?api_key=580966185e2883c73da7ba529a4ac3fe&query=" + act2_t1)
            data = response2.json()
            act2_t1Port = (data["results"][0]["popularity"])
            act2_t1Port = float(act2_t1Port)

            response3 = requests.get(
                "http://api.tmdb.org/3/search/person?api_key=580966185e2883c73da7ba529a4ac3fe&query=" + act3_t1)
            data = response3.json()
            act3_t1Port = (data["results"][0]["popularity"])
            act3_t1Port = float(act1_t1Port)

            response4 = requests.get(
                "http://api.tmdb.org/3/search/person?api_key=580966185e2883c73da7ba529a4ac3fe&query=" + d_t1)
            data = response4.json()
            d_t1Port = (data["results"][0]["popularity"])
            d_t1Port = float(d_t1Port)

            response5 = requests.get(
                "http://api.tmdb.org/3/search/person?api_key=580966185e2883c73da7ba529a4ac3fe&query=" + s_t1)
            data = response5.json()
            s_t1Port = (data["results"][0]["popularity"])
            s_t1Port = float(s_t1Port)

            response6 = requests.get(
                "http://api.tmdb.org/3/search/person?api_key=580966185e2883c73da7ba529a4ac3fe&query=" + act1_t2)
            data = response6.json()
            act1_t2Port = (data["results"][0]["popularity"])
            act1_t2Port = float(act1_t2Port)

            response7 = requests.get(
                "http://api.tmdb.org/3/search/person?api_key=580966185e2883c73da7ba529a4ac3fe&query=" + act2_t2)
            data = response7.json()
            act2_t2Port = (data["results"][0]["popularity"])
            act2_t2Port = float(act2_t2Port)

            response8 = requests.get(
                "http://api.tmdb.org/3/search/person?api_key=580966185e2883c73da7ba529a4ac3fe&query=" + act3_t2)
            data = response8.json()
            act3_t2Port = (data["results"][0]["popularity"])
            act3_t2Port = float(act1_t2Port)

            response9 = requests.get(
                "http://api.tmdb.org/3/search/person?api_key=580966185e2883c73da7ba529a4ac3fe&query=" + d_t2)
            data = response9.json()
            d_t2Port = (data["results"][0]["popularity"])
            d_t2Port = float(d_t2Port)

            response10 = requests.get(
                "http://api.tmdb.org/3/search/person?api_key=580966185e2883c73da7ba529a4ac3fe&query=" + s_t2)
            data = response10.json()
            s_t2Port = (data["results"][0]["popularity"])
            s_t2Port = float(s_t2Port)

            response11 = requests.get(
                "http://api.tmdb.org/3/search/person?api_key=580966185e2883c73da7ba529a4ac3fe&query=" + act1_t3)
            data = response11.json()
            act1_t3Port = (data["results"][0]["popularity"])
            act1_t3Port = float(act1_t3Port)

            response12 = requests.get(
                "http://api.tmdb.org/3/search/person?api_key=580966185e2883c73da7ba529a4ac3fe&query=" + act2_t3)
            data = response12.json()
            act2_t3Port = (data["results"][0]["popularity"])
            act2_t3Port = float(act2_t3Port)

            response13 = requests.get(
                "http://api.tmdb.org/3/search/person?api_key=580966185e2883c73da7ba529a4ac3fe&query=" + act3_t3)
            data = response13.json()
            act3_t3Port = (data["results"][0]["popularity"])
            act3_t3Port = float(act1_t3Port)

            response14 = requests.get(
                "http://api.tmdb.org/3/search/person?api_key=580966185e2883c73da7ba529a4ac3fe&query=" + d_t3)
            data = response14.json()
            d_t3Port = (data["results"][0]["popularity"])
            d_t3Port = float(d_t3Port)

            response15 = requests.get(
                "http://api.tmdb.org/3/search/person?api_key=580966185e2883c73da7ba529a4ac3fe&query=" + s_t3)
            data = response15.json()
            s_t3Port = (data["results"][0]["popularity"])
            s_t3Port = float(s_t3Port)

            if act1_t1tid == "":
                act1_t1ts = 50000.00

            else:
                responset = requests.get(
                    "http://api.twittercounter.com/?twitter_id=" + act1_t1tid + "&apikey=692d4f822384e3f429a4c998e4f91ad7")
                datat = responset.json()
                act1_t1ts = (datat["followers_yesterday"])
                act1_t1ts = float(act1_t1ts)

            print act1_t1ts

            if act2_t1tid == "":
                act2_t1ts = 50000.00
            else:
                responset = requests.get(
                    "http://api.twittercounter.com/?twitter_id=" + act2_t1tid + "&apikey=692d4f822384e3f429a4c998e4f91ad7")
                datat = responset.json()
                act2_t1ts = (datat["followers_yesterday"])
                act2_t1ts = float(act2_t1ts)

            if act3_t1tid == "":
                act3_t1ts = 50000.00

            else:
                responset = requests.get(
                    "http://api.twittercounter.com/?twitter_id=" + act3_t1tid + "&apikey=692d4f822384e3f429a4c998e4f91ad7")
                datat = responset.json()
                act3_t1ts = (datat["followers_yesterday"])
                act3_t1ts = float(act3_t1ts)

            if act1_t2tid == "":
                act1_t2ts = 50000.00

            else:
                responset = requests.get(
                    "http://api.twittercounter.com/?twitter_id=" + act1_t2tid + "&apikey=692d4f822384e3f429a4c998e4f91ad7")
                datat = responset.json()
                act1_t2ts = (datat["followers_yesterday"])
                act1_t2ts = float(act1_t2ts)

            if act2_t2tid == "":
                act2_t2ts = 50000.00
            else:

                responset = requests.get(
                    "http://api.twittercounter.com/?twitter_id=" + act2_t2tid + "&apikey=692d4f822384e3f429a4c998e4f91ad7")
                datat = responset.json()
                act2_t2ts = (datat["followers_yesterday"])
                act2_t2ts = float(act2_t2ts)

            if act3_t2tid == "":
                act3_t2ts = 50000.00

            else:
                responset = requests.get(
                    "http://api.twittercounter.com/?twitter_id=" + act3_t2tid + "&apikey=692d4f822384e3f429a4c998e4f91ad7")
                datat = responset.json()
                act3_t2ts = (datat["followers_yesterday"])
                act3_t2ts = float(act3_t2ts)

            if act1_t3tid == "":
                act1_t3ts = 50000.00

            else:
                responset = requests.get(
                    "http://api.twittercounter.com/?twitter_id=" + act1_t3tid + "&apikey=692d4f822384e3f429a4c998e4f91ad7")
                datat = responset.json()
                act1_t3ts = (datat["followers_yesterday"])
                act1_t3ts = float(act1_t3ts)

            if act2_t3tid == "":
                act2_t3ts = 50000.00

            else:
                responset = requests.get(
                    "http://api.twittercounter.com/?twitter_id=" + act2_t3tid + "&apikey=692d4f822384e3f429a4c998e4f91ad7")
                datat = responset.json()
                act2_t3ts = (datat["followers_yesterday"])
                act2_t3ts = float(act2_t3ts)

            if act3_t3tid == "":
                act3_t3ts = 50000.00

            else:
                responset = requests.get(
                    "http://api.twittercounter.com/?twitter_id=" + act3_t3tid + "&apikey=692d4f822384e3f429a4c998e4f91ad7")
                datat = responset.json()
                act3_t3ts = (datat["followers_yesterday"])
                act3_t3ts = float(act3_t3ts)


        except Exception as e:  # This is the correct syntax
            return render(request, "main.html")




        # main criteria vector
        slidervalue1 = slider1  # cast/director
        slidervalue2 = slider2  # director/scenarist
        slidervalue3 = slider3  # cast/scenarist

        castToDirector = 1 / slidervalue1
        directorToCast = slidervalue1
        directorToScenarist = 1 / slidervalue2
        scenaristToDirector = slidervalue2
        scenaristToCast = 1 / slidervalue3
        castToScenarist = slidervalue3

        maincriteriaMatrix = matrix([[1.0, castToDirector, castToScenarist], [directorToCast, 1.0, directorToScenarist],
                                     [scenaristToCast, scenaristToDirector, 1.0]])
        sumColumn1 = maincriteriaMatrix.item((0, 0)) + maincriteriaMatrix.item((1, 0)) + maincriteriaMatrix.item((2, 0))
        sumColumn2 = maincriteriaMatrix.item((0, 1)) + maincriteriaMatrix.item((1, 1)) + maincriteriaMatrix.item((2, 1))
        sumColumn3 = maincriteriaMatrix.item((0, 2)) + maincriteriaMatrix.item((1, 2)) + maincriteriaMatrix.item((2, 2))

        normalizedMCM = matrix([[maincriteriaMatrix.item((0, 0)) / sumColumn1,
                                 maincriteriaMatrix.item((0, 1)) / sumColumn2,
                                 maincriteriaMatrix.item((0, 2)) / sumColumn3],
                                [maincriteriaMatrix.item((1, 0)) / sumColumn1,
                                 maincriteriaMatrix.item((1, 1)) / sumColumn2,
                                 maincriteriaMatrix.item((1, 2)) / sumColumn3],
                                [maincriteriaMatrix.item((2, 0)) / sumColumn1,
                                 maincriteriaMatrix.item((2, 1)) / sumColumn2,
                                 maincriteriaMatrix.item((2, 2)) / sumColumn3]])
        normSumRow1 = normalizedMCM.item((0, 0)) + normalizedMCM.item((0, 1)) + normalizedMCM.item((0, 2))
        normSumRow2 = normalizedMCM.item((1, 0)) + normalizedMCM.item((1, 1)) + normalizedMCM.item((1, 2))
        normSumRow3 = normalizedMCM.item((2, 0)) + normalizedMCM.item((2, 1)) + normalizedMCM.item((2, 2))

        priorityVector = matrix([[normSumRow1 / 3], [normSumRow2 / 3], [normSumRow3 / 3]])
        ax = maincriteriaMatrix * priorityVector
        axDivx = matrix(
            [[ax.item((0, 0)) / priorityVector.item((0, 0))], [ax.item((1, 0)) / priorityVector.item((1, 0))],
             [ax.item((2, 0)) / priorityVector.item((2, 0))]])

        lambdamax = (axDivx.item((0, 0)) + axDivx.item((1, 0)) + axDivx.item((2, 0))) / 3
        ci = (lambdamax - 3) / (3 - 1)
        cr = ci / 0.58

        if (cr < 0.1):
            consistencyCheck = True
        else:
            consistencyCheck = False

        # sub criteria vector
        subslidervalue = subSlider

        portToPopu = subslidervalue
        popuToPort = 1 / subslidervalue

        subcriteriaMattrix = matrix([[1.0, popuToPort], [portToPopu, 1.0]])
        subsumColumn1 = subcriteriaMattrix.item((0, 0)) + subcriteriaMattrix.item((1, 0))
        subsumColumn2 = subcriteriaMattrix.item((0, 1)) + subcriteriaMattrix.item((1, 1))

        normalizedSCM = matrix(
            [[subcriteriaMattrix.item(0, 0) / subsumColumn1, subcriteriaMattrix.item(0, 1) / subsumColumn2],
             [subcriteriaMattrix.item(1, 0) / subsumColumn1, subcriteriaMattrix.item(1, 1) / subsumColumn2]])
        subPriorityVector = matrix([[normalizedSCM.item(0, 0)], [normalizedSCM.item(1, 1)]])

        # scenarist score --> normalized by case respectively
        s1 = s_t1Port
        s2 = s_t2Port
        s3 = s_t3Port

        scenaristSum = s1 + s2 + s3

        scenaristMatrix = matrix([[s1 / scenaristSum], [s2 / scenaristSum], [s3 / scenaristSum]])

        # director score --> normalized by case respectively
        d1 = d_t1Port
        d2 = d_t2Port
        d3 = d_t3Port

        directorSum = d1 + d2 + d3

        directorMatrix = matrix([[d1 / directorSum], [d2 / directorSum], [d3 / directorSum]])

        # cast score matrix

        # cast portfolio score
        a1t1 = act1_t1Port
        a2t1 = act2_t1Port
        a3t1 = act3_t1Port

        avgCast1 = (a1t1 + a2t1 + a3t1) / 3

        a1t2 = act1_t2Port
        a2t2 = act2_t2Port
        a3t2 = act3_t2Port

        avgCast2 = (a1t2 + a2t2 + a3t2) / 3

        a1t3 = act1_t3Port
        a2t3 = act2_t3Port
        a3t3 = act3_t3Port

        avgCast3 = (a1t3 + a2t3 + a3t3) / 3

        sumAVGs = avgCast1 + avgCast2 + avgCast3

        catPortfolioMatrix = matrix([[avgCast1 / sumAVGs], [avgCast2 / sumAVGs], [avgCast3 / sumAVGs]])

        # cast popularity score
        a1t1Pop = act1_t1ts
        a2t1Pop = act2_t1ts
        a3t1Pop = act3_t1ts

        avgCast1Pop = (a1t1Pop + a2t1Pop + a3t1Pop) / 3

        a1t2Pop = act1_t2ts
        a2t2Pop = act2_t2ts
        a3t2Pop = act3_t2ts

        avgCast2Pop = (a1t2Pop + a2t2Pop + a3t2Pop) / 3

        a1t3Pop = act1_t3ts
        a2t3Pop = act2_t3ts
        a3t3Pop = act3_t3ts

        avgCast3Pop = (a1t3Pop + a2t3Pop + a3t3Pop) / 3

        sumAVGsPop = avgCast1Pop + avgCast2Pop + avgCast3Pop

        castPopularityMatrix = matrix(
            [[avgCast1Pop / sumAVGsPop], [avgCast2Pop / sumAVGsPop], [avgCast3Pop / sumAVGsPop]])

        # cast/popularity-portfolio matrix
        popPopMatrix = matrix([[castPopularityMatrix.item(0, 0), catPortfolioMatrix.item(0, 0)],
                               [castPopularityMatrix.item(1, 0), catPortfolioMatrix.item(1, 0)],
                               [castPopularityMatrix.item(2, 0), catPortfolioMatrix.item(2, 0)]])
        castScoreMatrix = matrix(popPopMatrix * subPriorityVector)

        # final Matrix
        finalMatrix = ([[castScoreMatrix.item(0, 0), directorMatrix.item(0,0), scenaristMatrix.item(0,0)], [castScoreMatrix.item(1, 0), directorMatrix.item(1,0), scenaristMatrix.item(1,0)],
                        [castScoreMatrix.item(2, 0), directorMatrix.item(2,0), scenaristMatrix.item(2,0)]])
        finalResult = finalMatrix * priorityVector

        fig = Figure()
        ax = fig.add_subplot(111)
        x = []
        y = []

        x.append(float(b_t1))
        x.append(float(b_t2))
        x.append(float(b_t3))

        y.append(finalResult.item(0,0))
        y.append(finalResult.item(1,0))
        y.append(finalResult.item(2,0))

        ax.plot(x, y, '*')
        ax.text(float(b_t1), finalResult.item(0,0), "Team1\n" , fontsize=10)
        ax.text(float(b_t2), finalResult.item(1,0), "Team2\n" , fontsize=10)
        ax.text(float(b_t3), finalResult.item(2,0), "Team3\n" , fontsize=10)
        ax.set_ylabel("Success Rate", fontsize=15)
        ax.set_xlabel("Budget (in Millions)", fontsize=15)

        canvas = FigureCanvas(fig)
        response = HttpResponse(content_type='image/png')
        canvas.print_png(response)
        return response

    return render(request, "main.html")
