!!README!!

=プログラム名=
カード認識プログラム

=実行環境=
Mac OS X El Capitan 10.11.5
python 2.7

=必要なライブラリ=
PIL
sqlite3

=準備と仕様=
・「__init__.py」の「local_place」を「Ygopro」が置かれているディレクトリに指定
・カード全体を含んだ画像を用意(正方形に切り取っているなら絵の部分でもいけるかも)
　できればスキャナで取り込んだ画像が望ましい
・「recog.py」内の61,62行目付近で日本語版か英語版のcdbを選択する
　日本語版を選択している場合は、「Ygopro」内に別のcdbを用意し、
　62行目の部分を書き換えること
・「data.txt」は、全てのカード画像を事前にhash化させたもの。
	追加更新する場合は、「python append_data.py」でおそらくうまくいく（まだ試してない）


=使い方=
・全カード情報から探したい場合
python recog.py "認識したい画像ファイル名"

・デッキ内に絞って探したい場合
python recog.py "認識したい画像ファイル名" "デッキ名(〇〇.ydk)"


=入出力例=
#状態
Ygoproのdeck内に「silentgrave.ydk」が入っており、
ecog.pyと同ディレクトリに「dp17-jp002.jpg」(沈黙の魔術師-サイレント・マジシャン)がある
cdbは日本語版を利用

#入力
>> python recog.py dp17-jp002.jpg silentgrave.ydk

#出力
カード番号:
41175645

カード名:
Silent Magician

カード効果:
Cannot be Normal Summoned/Set. Must be Special Summoned (from your hand) by Tributing 1 Spellcaster-Type monster, and cannot be Special Summoned by other ways. This card gains 500 ATK for each card in your hand. Once per turn, during either player's turn, when a Spell Card is activated: You can negate the activation. If this card is destroyed by battle, or if this card in its owner's control is destroyed by an opponent's card effect: You can Special Summon 1 "Silent Magician" monster from your hand or Deck, except "Silent Magician", ignoring its Summoning conditions.