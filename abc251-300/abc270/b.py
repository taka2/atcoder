# -*- coding: utf-8 -*-
x,y,z = map(int, input().split())

if x > 0:
    # ゴールが正の場合
    if y > 0 and y < x:
        # 壁が途中にある場合
        if z < y:
            # ハンマーが壁の手前にある場合
            if z < 0:
                # ハンマーがマイナス座標にある場合
                print(x + abs(z)*2)
            else:
                print(x)
        else:
            print(-1)
    else:
        # 壁が途中にない場合
        print(x)
else:
    # ゴールが負の場合
    if y < 0 and y > x:
        # 壁が途中にある場合
        if z > y:
            # ハンマーが壁の手前にある場合
            if z > 0:
                #ハンマーがプラス座標にある場合
                print(abs(x) + z*2)
            else:
                print(abs(x))
        else:
            print(-1)
    else:
        # 壁が途中にない場合
        print(abs(x))