# 掲示板サイト作成時、詰まったところメモ

## タイトルには画像を投稿可能にしたいが、投稿しなくてもよいようにしたい

画像付きのスレッドを立てられるようにしたいが、同時に画像なしのスレッドも立てられるようにしたい。DBには画像のpathを文字列型で保存するようにする。
Djangoでは、なにも指定せずにmodelを作成すると、not null制約がかかる。
なので、`null=True`をmodelのカラムにオプションでつける必要がある。ただし、このオプションでは、空白をnullと判定できるデータ型のみに依存するため、**整数型、ブール型**がこのオプションで対応できる。
文字列型は、空白・未入力項目を**blank**として判定するため、`blank=True`オプションを指定する必要がある。
